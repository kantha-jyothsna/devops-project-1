from http.server import BaseHTTPRequestHandler, HTTPServer
import os

APP_ENV = os.getenv("APP_ENV", "development")
APP_VERSION = os.getenv("APP_VERSION", "1.0")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = f"""
        <html>
        <head>
            <title>DevOps Project 1</title>
        </head>
        <body>
            <h1>My DevOps Application</h1>
            <p>Environment: {APP_ENV}</p>
            <p>Version: {APP_VERSION}</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(response.encode())

    def log_message(self, format, *args):
        print(f"Request: {args}")


server = HTTPServer(("0.0.0.0", 5000), Handler)

print("Application running on port 5000")
print(f"Environment: {APP_ENV}")
print(f"Version: {APP_VERSION}")

server.serve_forever()
