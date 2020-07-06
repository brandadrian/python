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
CONFIG_SHELLYAUTHORIZATION = 'shelly-authorization-token'
CONFIG_APIAUTHORIZATION = 'api-authorization-token'

class requestHandler(BaseHTTPRequestHandler):
    ###GET
    def do_GET(self):
        log('GET; ' + self.path + '; IP; ' + self.client_address[0])

        try:
            config = getConfig()
            isAuthenticated = self.headers.get('Authorization') == 'Basic ' + config[CONFIG_APIAUTHORIZATION]

            if (self.path.endswith('/home-automation')):
                send_response(self, 'interface to home automation devices', 200)

            elif (self.path.endswith('/home-automation/shelly')):
                send_response(self, 'interface to shelly devices', 200)

            elif (self.path.endswith('/home-automation/shelly/relay/0')):
                if (isAuthenticated):
                    request = requests.get(config[CONFIG_SHELLYURL] + config[CONFIG_SHELLYRELAY0], headers={'Authorization': 'Basic ' + config[CONFIG_SHELLYAUTHORIZATION]})
                    send_response(self, request.text, 200)
                else:
                    send_response(self, 'not authenticated for shelly', 401)

            elif (self.path.endswith('/home-automation/shelly/relay/42')):
                request = requests.get(config[CONFIG_SHELLYURL] + config[CONFIG_SHELLYRELAY0], headers={'Authorization': 'Basic ' + config[CONFIG_SHELLYAUTHORIZATION]})
                send_response(self, request.text, 200)

            elif (self.path.endswith('/server-state')):
                send_response(self, 'server running', 200)

            elif (self.path.endswith('/status')):
                f=open("httpServerLog.txt", "r")
                logLines = f.readlines()
                logLines.reverse()
                f.close() 
                send_response(self, logLines, 200)

            else:
                self.send_response(404)                
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
    
def send_response(self, message, code):
    self.send_response(code)
    self.send_header('Content-type', 'application/json')
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Credentials', 'true')
    
    self.end_headers()
    self.wfile.write(json.dumps({'message': message}).encode('utf-8'))

serve()
