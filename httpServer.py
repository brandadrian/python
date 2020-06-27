from http.server import HTTPServer, BaseHTTPRequestHandler

class requestHandler(BaseHTTPRequestHandler):
    ###GET
    def do_GET(self):
        try:
            if (self.path.endswith('/cars')):
                self.send_response(200)
            else:
                self.send_response(404)
            self.end_headers()
        except:
            error =  sys.exc_info()[0]
            print("Unexpected error:", error)
            self.send_response(500)
            self.end_headers()

    ###POST
    def do_POST(self):
        try:
            if (self.path.endswith('/cars')):
                content_len = int(self.headers.get('Content-Length'))
                post_body = self.rfile.read(content_len)
                self.send_response(200)
                print(post_body)
            else:
                self.send_response(404)
            self.end_headers()
        except:
            error =  sys.exc_info()[0]
            print("Unexpected error:", error)
            self.send_response(500)
            self.end_headers()

def serve():
    PORT = 8000
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, requestHandler)
    print('Server running on port: ', PORT)
    server.serve_forever()

serve()
