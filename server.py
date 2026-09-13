"""
AI Waste Segregation Guide - Local Development Server
Lightweight Python 3.11 HTTP Server with automatic port negotiation,
clean MIME types, and instant browser launch.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

DEFAULT_PORT = 8000
MAX_PORT_ATTEMPTS = 20

class CustomHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS and disable caching for instant development iterations
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def guess_type(self, path):
        # Ensure correct JavaScript module and CSS MIME types on Windows
        if path.endswith('.js'):
            return 'application/javascript'
        if path.endswith('.css'):
            return 'text/css'
        if path.endswith('.json'):
            return 'application/json'
        if path.endswith('.svg'):
            return 'image/svg+xml'
        return super().guess_type(path)

def find_available_port(start_port):
    import socket
    port = start_port
    for _ in range(MAX_PORT_ATTEMPTS):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
        port += 1
    return start_port

import threading
import time

def open_browser_delayed(url):
    time.sleep(0.5)
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"[WARN] Could not automatically open browser: {e}", flush=True)

def run_server():
    # Configure UTF-8 for console output on Windows to avoid UnicodeEncodeError
    if sys.platform == 'win32':
        import io
        try:
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
            sys.stderr.reconfigure(encoding='utf-8', errors='replace')
        except AttributeError:
            pass

    # Change directory to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    port = find_available_port(DEFAULT_PORT)
    url = f"http://127.0.0.1:{port}/index.html"

    print("=" * 70, flush=True)
    print(" [AI WASTE SEGREGATION GUIDE] LOCAL SERVER ACTIVE", flush=True)
    print("=" * 70, flush=True)
    print(f" URL:         {url}", flush=True)
    print(f" Directory:   {script_dir}", flush=True)
    print(f" Python:      {sys.version.split()[0]}", flush=True)
    print(" Press Ctrl+C to terminate the server at any time.", flush=True)
    print("=" * 70, flush=True)

    socketserver.TCPServer.allow_reuse_address = True
    server_cls = getattr(http.server, 'ThreadingHTTPServer', socketserver.ThreadingTCPServer)

    try:
        with server_cls(("127.0.0.1", port), CustomHTTPHandler) as httpd:
            # Launch browser in background thread so it doesn't block server loop
            threading.Thread(target=open_browser_delayed, args=(url,), daemon=True).start()
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[INFO] Server stopped by user.", flush=True)
    except Exception as e:
        print(f"\n[ERROR] Server error: {e}", flush=True)

if __name__ == '__main__':
    run_server()
