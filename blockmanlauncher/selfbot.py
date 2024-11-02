import socket
import json
from .config import API_URL

class selfbot:
    def __init__(self):
        self.access_token = None
        self.user_id = None

    def bl(self, token, user_id):
        self.access_token = token
        self.user_id = user_id

        if not self.access_token or not self.user_id:
            print("Error: Access token and user ID must be set before connecting.")
            return
        
        api_url_parts = API_URL.split("://")
        host_port = api_url_parts[1].split(":")
        host = host_port[0]
        port = int(host_port[1])

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                print(f"Connected to API at {API_URL}")

                payload = {
                    "access_token": self.access_token,
                    "user_id": self.user_id,
                    "endpoint": "/api/v1/selfbot"
                }
                message = json.dumps(payload)

                s.sendall(message.encode('utf-8'))
                print(f"Sent message: {message}")

                response = s.recv(1024)
                print(f"Received response: {response.decode('utf-8')}")
        
        except Exception as e:
            print(f"Error: {e}")