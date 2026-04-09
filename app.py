// Fixed pattern
from flask import Response
response = Response()
external_link_tag = "X-XSS-Protection: 1; mode=block"
response.headers.extend({'X-XSS-Protection': external_link_tag}) # Set the X-XSS-Protection header to '1; mode=block' to enable protection against Cross-Site Scripting (XSS)