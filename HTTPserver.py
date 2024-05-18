from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime


HOST = "192.168.42.8"
PORT = 9999

class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()        

        self.wfile.write(bytes("<html><body><h1>vicracker</h1></body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = datetime.now().strftime('%H:%M:%S')
        self.wfile.write(bytes(f"Time: {date}", "utf-8"))



server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server running")
server.serve_forever()
server.server_close()
