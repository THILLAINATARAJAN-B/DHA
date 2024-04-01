import http.server
import socketserver
import pyautogui as pi
with socketserver.TCPServer(("",80),http.server.SimpleHTTPRequestHandler) as server:
    server.serve_forever()
py.press(('t','h','i','l','l','a','i',' ','o','r','u',' ','l','o','o','s','u',' ','k','o','o','t','h','i'))