#!/usr/bin/python3
"""
A simple HTTP server using Python's http.server module.

This server handles basic GET requests and responds with either plain text or
JSON data depending on the endpoint accessed.

Endpoints:
    - `/`: Returns a simple text message.
    - `/data`: Returns a JSON object with sample data.
    - `/status`: Returns a simple "OK" message to indicate the server's status.
    - `/info`: Returns version and description of the API in JSON format.
    - Any other endpoint: Returns a 404 error with an "Endpoint not found"
      message.
"""

from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json


class SimpleHTTPServer(BaseHTTPRequestHandler):
    """A simple HTTP server to handle GET requests."""

    def do_GET(self):
        """Handle GET requests for different endpoints."""
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        if path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())

        elif path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Error: Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleHTTPServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == "__main__":
    run()
