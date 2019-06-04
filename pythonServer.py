import socket

host, port = '127.0.0.1', 8011

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Server running on", host , ":", port)

while True:
    sock.listen(5)
    (client, address) = sock.accept()
    client.settimeout(60)

    data = client.recv(1024).decode()

    print(data)

    file_requested = data.split(' ')[1]

    
    if file_requested == "/":
        file_requested = "/index.html"

    file_path = 'public_html' + file_requested

    try:
        response_header = b"HTTP/1.1 200 OK\n\n"
        f = open(file_path, 'rb')
        response_data = f.read()
        f.close()
        print("Requested File : " + file_path)


    except FileNotFoundError:
        response_header = b"HTTP/1.1 404 Not Found\n\n"
        response_data = b"<h1>Error 404 - File Not Found<h1>"


    response = response_header + response_data


    client.send(response)
    client.close()

