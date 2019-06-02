import BaseHTTPServer, CGIHTTPServer;
s = BaseHTTPServer.HTTPServer(('', 80), CGIHTTPServer.CGIHTTPRequestHandler);
s.serve_forever()
