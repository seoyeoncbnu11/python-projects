import socket

in_addr = socket.gethostbyname(socket.gethostname())

print(in_addr)

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print(in_addr.getsockname()[0])
