import nmap

scanner = nmap.PortScanner()

print('welcome, nmap automation tool')
print('<-------------------------------->')

ip_address = input('enter ip you want to scan: ')
print(f"ip address is: {ip_address}")

response = int(input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan
                4)OS scan\n"""))
# print(response)

if response == 1:
    print('1)SYN ACK Scan')
    print(f"nmap version: {scanner.nmap_version()}")
    scanner.scan(ip_address, '1-1080', '-v -sS')
    print(scanner.scaninfo())
    print(f"ip status: {scanner[ip_address].state()}")
    print(scanner[ip_address].all_protocols())
    print("open ports: ", scanner[ip_address]['tcp'].keys())
elif response == 2:
    print('2)UDP Scan')
    print(f"nmap version: {scanner.nmap_version()}")
    scanner.scan(ip_address, '1-1080', '-v -sU')
    print(scanner.scaninfo())
    print(f"ip status: {scanner[ip_address].state()}")
    print(scanner[ip_address].all_protocols())
    print("open ports: ", scanner[ip_address]['udp'].keys())
elif response == 3:
    print('3)Comprehensive Scan')
    print(f"nmap version: {scanner.nmap_version()}")
    scanner.scan(ip_address, '1-1080', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print(f"ip status: {scanner[ip_address].state()}")
    print(scanner[ip_address].all_protocols())
    print("open ports: ", scanner[ip_address]['tcp'].keys())
elif response == 4:
    print('4)OS scan')
    print(scanner.scan(ip_address, arguments="-O")['scan'][ip_address]['osmatch'][0])
    print(scanner.scan(ip_address, arguments="-O")['scan'][ip_address]['osmatch'][1])
else:
    print('invalid option')