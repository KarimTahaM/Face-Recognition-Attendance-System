import subprocess
import webbrowser
import time
import os
import http.server
import socketserver
import threading

def run_frontend_server():
    # Change to the static directory
    os.chdir(os.path.join(os.path.dirname(__file__), 'static'))
    
    # Create HTTP server
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 8080), Handler) as httpd:
        print("Frontend server started at http://localhost:8080")
        httpd.serve_forever()

# Start the FastAPI backend
backend_process = subprocess.Popen(
    ["uvicorn", "api:app", "--host", "127.0.0.1", "--port", "8000"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Start the frontend server in a separate thread
frontend_thread = threading.Thread(target=run_frontend_server, daemon=True)
frontend_thread.start()

# Wait a few seconds to ensure both servers start
time.sleep(3)

# Open the frontend in the default web browser
webbrowser.open("http://localhost:8080/webcam_client.html")

print("Services started. Press Ctrl+C to stop.")

try:
    # Keep the main thread alive
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down...")
    backend_process.terminate()