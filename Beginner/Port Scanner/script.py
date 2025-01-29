import socket


def port_scanner(target_ip, startport, endport):
    print(f"Scanning IP: {target_ip}")

    for port in range(start_port, end_port + 1):
        try:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sock.settimeout(0.5)

            result = sock.connect_ex((target_ip, port))

            if result == 0:
                print(f"Port {port}: Open")
            else:
                print(f"Port {port}: Closed")

            sock.close()
        except socket.error as e:
            print(f"Error scanning port: {port}: {e}")


target_ip = input("Enter target IP: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

port_scanner(target_ip, start_port, end_port)