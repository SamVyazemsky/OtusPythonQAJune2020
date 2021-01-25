import socket
import json

HOST = '127.0.0.1'
PORT = 4335
BUFFER_SIZE = 2048

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Started socket on", s)
    s.listen()
    connect, url = s.accept()

    with connect:
        print('Connected by', url)
        while True:
            data = connect.recv(BUFFER_SIZE).decode("utf-8").strip()
            if data:
                http_request_headers: dict = {}
                headers = data.split(sep="\r\n")
                for i, header in enumerate(headers):
                    if i == 0:
                        continue
                    header_name = header.split(sep=":")[0].strip()
                    header_value = header.split(sep=":")[1].strip()
                    http_request_headers[header_name] = header_value
                content = json.dumps(http_request_headers)
                connect.send(f"HTTP/1.1 200 OK\n Content-Length: 100\n Connection: close\n "
                          f"Content-Type: application/json \n\n {content}".encode("utf-8"))
                break
