import http.server
import socketserver

ACCESS = 8000

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("",ACCESS), Handler)
print("Server at ACCESS" ,ACCESS)
httpd.serve_forever()
