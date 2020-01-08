import os
from io import BytesIO
import urllib
from http.server import BaseHTTPRequestHandler

class HTTPRequestHeader(BaseHTTPRequestHandler):
    __query_string = None
    __http_header_dir = None

    def __init__(self, http_header_dir):
        self.__http_header_dir = http_header_dir
        self.__read_header()

    def __read_header(self):
        header_file = os.path.join(self.__http_header_dir, 'request.head')
        try:
            if os.path.exists(header_file):
                with open(header_file, 'rb') as fd:
                    self.rfile = fd
                    self.error_code = self.error_message = None
                    self.raw_requestline = self.rfile.readline()
                    self.parse_request()
                    self.parser_query_string()
                    self.send_header("REQUEST_METHOD", "POST")
            else:
                print("Http Request - Read Header {0}".format(header_file))
                raise FileNotFoundError
        except IOError as e:
            print("Http Request - Read Header {0}".format(e))
            raise FileNotFoundError

    def parser_query_string(self):
        try:
            q_string = self.path.split("?")[1]
            self.query_string = urllib.parse.parse_qs(q_string)
        except Exception as e:
            pass

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message

    @property
    def host(self):
        return self.headers.get('host')

    @property
    def query_string(self):
        return self.__query_string

    @query_string.setter
    def query_string(self, val):
        self.__query_string = val

    @property
    def method(self):
        return self.command 



if __name__ == '__main__':
    request_header = HTTPRequestHeader("./")
    print(request_header.host)
    print(request_header.path)
    print(request_header.query_string)
    print(request_header.method)
