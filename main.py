# Contact: OWoodflint@gmail.com
# This script starts a basic web server and redirects all requests
# to https://www.obscura.ccstiet.com

from http.server import BaseHTTPRequestHandler, HTTPServer

class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(301)
        self.send_header('Location', 'https://www.obscura.ccstiet.com')
        self.end_headers()

if __name__ == "__main__":
    port = 8080
    print(f"Starting redirect server on port {port}...")
    server = HTTPServer(('', port), RedirectHandler)
    server.serve_forever()
