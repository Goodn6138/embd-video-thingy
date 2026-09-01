from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()

            self.wfile.write(
                json.dumps({
                    "status": "ok"
                }).encode("utf-8")
            )
            return

        self.send_response(404)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(
            json.dumps({
                "error": "Not found"
            }).encode("utf-8")
        )

