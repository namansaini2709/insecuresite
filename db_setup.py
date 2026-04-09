import sqlite3
import os
import ssl

DB_PATH = 'shopeasy.db'

def setup_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        
    # Use the highest TLS version supported by Python
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    
    conn = sqlite3.connect(DB_PATH, ssl_context=context)
    c = conn.cursor()
    
    # ... (rest of the code remains the same) 