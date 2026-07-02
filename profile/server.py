import http.server
import os
import socketserver
import webbrowser

HOST = "127.0.0.1"
PORT = 8000

os.chdir(os.path.dirname(os.path.abspath(__file__)))
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), handler) as httpd:
    url = f"http://{HOST}:{PORT}/"
    print(f"Private server running at {url} (accessible only from this machine)")
    print("Press Ctrl+C to stop.")
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
