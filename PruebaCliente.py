import socket
import json

data = {"origen": "Vaulx-en-Velin La Soie A", "destino": "Perrache A"}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect(('localhost', 12345))
        s.sendall(json.dumps(data).encode())
        response = s.recv(4096).decode()
        print(response)
    except Exception as e:
        print(f"Error: {e}")