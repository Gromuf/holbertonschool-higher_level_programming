#!/usr/bin/python3
"""
A simple HTTP server using Python's http.server module.

This server handles basic GET requests and responds with either plain text or
JSON data depending on the endpoint accessed.

Endpoints:
    - `/`: Returns a simple text message.
    - `/data`: Returns a JSON object with sample data.
    - `/status`: Returns a simple "OK" message to indicate the server's status.
    - Any other endpoint: Returns a 404 error with an "Endpoint not found"
      message.
"""

import http.server
import socketserver
import json


class SimpleHTTPServer(http.server.BaseHTTPRequestHandler):
    """A simple HTTP server to handle GET requests."""

    def do_GET(self):
        """Handle GET requests for different endpoints."""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Error: Endpoint not found")


PORT = 8000

with socketserver.TCPServer(("", PORT), SimpleHTTPServer) as server:
    print("serving at port {}".format(PORT))
    server.serve_forever()
