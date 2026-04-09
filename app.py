from flask import Flask, Response
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-SWF-Disable'] = True
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'no-referrer'
    return response
from flask import Flask, Response
app = Flask(__name__)
appp.get('/')(lambda: add_security_headers(Response('Hello World')))
