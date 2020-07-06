###########################################
#Python service for brand-api
#Autho: Adrian Brand
#Descripion:
#Web service to connect to home automation
###########################################

from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import json
import ssl
import requests
import configparser 

CONFIG_PORT = 'port'
CONFIG_SHELLYURL = "shelly-url"
CONFIG_SHELLYRELAY0 = 'shelly-relay0'
CONFIG_SHELLYAUTHORIZATION = 'authorization-token'

class requestHandler(BaseHTTPRequestHandler):
    ###GET
    def do_GET(self):
        log('GET; ' + self.path + '; IP; ' + self.client_address[0])
        try:
            config = getConfig()

            if (self.path.endswith('/home-automation')):
                receive_GET(self, 'interface to home automation devices')
            elif (self.path.endswith('/home-automation/shelly')):
                receive_GET(self, 'interface to shelly devices')
            elif (self.path.endswith('/home-automation/shelly/relay/0')):
                request = requests.get(config[CONFIG_SHELLYURL] + config[CONFIG_SHELLYRELAY0], headers={'Authorization': 'Basic ' + config[CONFIG_SHELLYAUTHORIZATION]})
                receive_GET(self, request.text)
            elif (self.path.endswith('/server-state')):
                receive_GET(self, 'server running')
            elif (self.path.endswith('/status')):
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                f=open("httpServerLog.txt", "r")
                logLines = f.readlines()
                logLines.reverse()
                f.close()  
                for logLine in logLines:
                	self.wfile.write(json.dumps({'message': logLine}).encode('utf-8'))
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
        log('POST; ' + self.path + '; IP; ' + self.client_address[0])
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
    PORT = int(getConfig()[CONFIG_PORT])
    server_address = ('', PORT)
    server = HTTPServer(server_address, requestHandler)
    print('Server running on port: ', PORT)
    log('server started on port: ' + str(PORT))
    server.serve_forever()

def log(message):
    dateTimeObj = datetime.now()
    messageInternal = dateTimeObj.strftime("%m/%d/%Y, %H:%M:%S") + "; " + message + '\n'
    f = open("httpServerLog.txt", "a")
    f.write(messageInternal)
    f.close()

def getConfig():
    config = configparser.RawConfigParser()
    config.read('config.txt')
    return dict(config.items('server-config'))
    
def receive_GET(self, message):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()
    self.wfile.write(json.dumps({'message': message}).encode('utf-8'))

serve()
