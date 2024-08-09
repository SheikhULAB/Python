import socket

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False
ip_address = input("Enter an IP Adress: ")
if is_valid_ip(ip_address):
    print("Valid IP address")
else:
    print("Invalid ip address")        