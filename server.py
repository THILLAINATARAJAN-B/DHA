import http.server
import socketserver

with socketserver.TCPServer(("",80),http.server.SimpleHTTPRequestHandler) as server:
    server.serve_forever()