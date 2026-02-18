from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import sys

LOG_FILE = "/app/logs/access.log"

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Get client IP address
            client_ip = self.client_address[0]

            # Get current date and time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Create log entry
            log_entry = f"{current_time} - IP: {client_ip}"

            with open(LOG_FILE, "a") as f:
                f.write(log_entry + "\n")

            # Print to stdout for docker logs
            print(log_entry, flush=True)

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Success: Log entry written successfully\n")

        except Exception as e:
            error_msg = f"Error: Failed to write log entry - {str(e)}"
            print(error_msg, file=sys.stderr, flush=True)

            self.send_response(500)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(f"{error_msg}\n".encode())

    def log_message(self, format, *args):
        # Override to customize or suppress default logging
        return

def run_server(port=5050):
    server_address = ("0.0.0.0", port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Python server running on port {port}", flush=True)
    print(f"Logging to: {LOG_FILE}", flush=True)
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()

