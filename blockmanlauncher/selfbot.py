import socket
import json
from .config import API_URL

class SelfBot:
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

                user_data = {
                    "id": self.user_id,
                    "accessToken": self.access_token
                }
                user_data_json = json.dumps(user_data)

                request_message = (
                    f'POST /api/v1/selfbot HTTP/1.1\r\n'
                    f'Host: {host}\r\n'
                    f'Content-Type: application/json\r\n'
                    f'Content-Length: {len(user_data_json)}\r\n'
                    f'\r\n'
                    f'{user_data_json}'
                )

                print(f'Sending: {request_message}')
                s.sendall(request_message.encode('utf-8'))

                response = s.recv(4096)
                print(f'Received response: {response.decode("utf-8")}')
        
        except Exception as e:
            print(f"Error: {e}")