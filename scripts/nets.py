import socket
import threading
import json
from utils import is_raw_data_piece


IP = "192.168.114.180"
PORT = 80

raw_data = []
lock = threading.Lock()


def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")

    while True:
        data_piece = client_socket.recv(4096).decode()
        print(f"Received data: {data_piece}")
        if not data_piece:
            print("Closing connection")
            break
        client_socket.send("Data received".encode())

        if is_raw_data_piece(data_piece):
            print("Data piece is valid")
            data_piece = json.loads(data_piece)
            with lock:
                replaced = False
                in_same_game = True
                for i, p in enumerate(raw_data):
                    if not (p['SID'] == data_piece['SID'] and p['GID'] == data_piece['GID']):
                        print("Data piece is not in the same game as those in raw_data")
                        in_same_game = False
                        break
                    if p['PlayerId'] == data_piece['PlayerId']:
                        raw_data[i] = data_piece
                        replaced = True
                        break
                if in_same_game and not replaced:
                    raw_data.append(data_piece)
                if len(raw_data) == 4:
                    sid = raw_data[0]['SID']
                    gid = raw_data[0]['GID']
                    with open(f"raw_data/S{sid}/G{gid}.json", 'w') as f:
                        json.dump(raw_data, f)
                    print(f"Saved raw data of S{sid}/G{gid}.json")
                    raw_data.clear()
        else:
            print("Data is invalid")

    client_socket.close()


def start_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(5)
    print(f"Server started at {ip}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()


if __name__ == "__main__":
    start_server(IP, PORT)
