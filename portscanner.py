import socket
import termcolor

def scan(target, ports):
    print('\n' + "Scanning: " + str(target))
    for port in range(1, ports + 1):
        scan_port(target, port)

def scan_port(ip_address, port):
    try:
        sock =socket.socket()
        sock.connect((ip_address, port))
        print("[+] Port Opened " + str(port))
    except:
        pass

    targets = input("[*] Enter Target to Scan(Split them by ,) : ")
    ports=input("[*] Enter How Many Ports You Want To Scan: ")
    if ',' in targets:
        print(term.color.colored(("[*] Scanning Multiple Targets "), 'green'))
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(' '), ports)
    else:
        scan(targets,ports)