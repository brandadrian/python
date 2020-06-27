from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import json
import ssl

class requestHandler(BaseHTTPRequestHandler):
    ###GET
    def do_GET(self):
        log('GET: ' + self.path)
        try:
            if (self.path.endswith('/cars')):
                self.send_response(200)
            elif (self.path.endswith('/seppli')):
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'hoi seppli!'}).encode('utf-8'))
            elif (self.path.endswith('/status')):
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                f=open("/volume1/homes/brandadr/tasks/httpServerLog.txt", "r")
                logLines = f.readlines()
                logLines.reverse()
                f.close()  
                for logLine in logLines:
                	self.wfile.write(logLine.encode('utf-8'))
            else:
                self.send_response(404)
            self.end_headers()
        except:
            error =  sys.exc_info()[0]
            log("Unexpected error; " + error)
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
    PORT = 8112
    server_address = ('192.168.1.109', PORT)
    server = HTTPServer(server_address, requestHandler)
    print('Server running on port: ', PORT)
    log('server started on port: ' + str(PORT))
    server.serve_forever()

def log(message):
    dateTimeObj = datetime.now()
    messageInternal = dateTimeObj.strftime("%m/%d/%Y, %H:%M:%S") + "; " + message + '\n'
    f = open("/volume1/homes/brandadr/tasks/httpServerLog.txt", "a")
    f.write(messageInternal)
    f.close()    

serve()
