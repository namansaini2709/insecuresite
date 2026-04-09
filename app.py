// Secure code pattern 
 from flask import make_response
 response = make_response('Hello World')
 response.headers['Content-Security-Policy'] = 'default-src http: https:;
 object-src 'none'
'
 response.headers['X-XSS-Protection'] = 1
 response.headers['X-Frame-Options'] = 'SAMEORIGIN'
 response.headers['.Strict-Transport-Security'] = 'max-age=31536000'