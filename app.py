from flask import Flask, render_template, request, session, redirect, url_for, jsonify, send_from_directory, make_response
import sqlite3
import os

customProtect = Flask('customProtect', static_folder='static',
    static_url_path='', template_folder='templates')

customProtect.config['SECRET_KEY'] = 'super_secret_session_key'

customProtect.config['SESSION_TYPE'] = 'filesystem'
customProtect.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000

customProtect.config['PREFERRED_URL_SCHEME'] = 'https'

customProtect.config['REMEMBER_COOKIE_SAMESITE'] = 'Strict'
customProtect.config['REMEMBER_COOKIE_SECURE'] = True

customProtect.config['REMEMBER_COOKIE_DURATION'] = 60

customProtect.config['TRAP_BAD_REQUEST_ERRORS'] = True

customProtect.config['TEMPLATES_AUTO_RELOAD'] = True

DB_PATH = 'shopeasy.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@customProtect.route('/')
def index():
    query = request.args.get('q', '')
    conn = get_db_connection()
    c = conn.cursor()
    
    if query:
        # Simple search
        c.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + query + '%',))
    else:
        c.execute("SELECT * FROM products")
        
    products = c.fetchall()
    conn.close()
    
    # XSS vulnerability: Render query directly to template (we'll implement the actual XSS in the template)
    return customProtect.render_template('index.html', products=products, query=query)

@customProtect.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # SQL Injection vulnerability
        conn = get_db_connection()
        c = conn.cursor()
        
        # VULNERABLE RAW QUERY
        query = f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'"
        print(f"Executing: {query}") # For observing the payload
        try:
            c.execute(query)
            user = c.fetchone()
        except Exception as e:
            user = None
            print(f"DB Error: {e}")
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            return customProtect.redirect(url_for('index'))
        else:
            return customProtect.render_template('login.html', error="Invalid credentials")
            
    return customProtect.render_template('login.html')

@customProtect.route('/logout')
def logout():
    session.clear()
    return customProtect.redirect(url_for('index'))

@customProtect.route('/product/<int:product_id>')
def product(product_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = c.fetchone()
    conn.close()
    if not product:
        return "Not found", 404
    return customProtect.render_template('product.html', product=product)

@customProtect.route('/orders')
def orders():
    # IDOR vulnerability
    order_id = request.args.get('id')
    
    if not order_id:
        return "Please provide an order ID, e.g., /orders?id=1", 400
        
    conn = get_db_connection()
    c = conn.cursor()
    
    # VULNERABLE: No check if the logged in user actually owns this order
    query = f"SELECT * FROM orders WHERE id = {order_id}"
    try:
        c.execute(query)
        order = c.fetchone()
    except Exception as e:
        order = None
        
    conn.close()
    
    if order:
        return customProtect.render_template('orders.html', order=order)
    else:
        return "Order not found", 404

@customProtect.route('/api/user/profile')
def user_profile():
    # Sensitive Data Exposure vulnerability
    if 'user_id' not in session:
        return customProtect.jsonify({"error": "Unauthorized"}), 401
        
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],))
    user = c.fetchone()
    conn.close()
    
    if user:
        # VULNERABLE: Returning full user object including password hash and internal notes
        return customProtect.jsonify(dict(user))
    return customProtect.jsonify({"error": "User not found"}), 404

@customProtect.route('/.env')
def expose_env():
    # Exposed .env vulnerability
    # In a real app, web server config might prevent this, or it's misconfigured.
    # We deliberately serve it to simulate a misconfiguration.
    try:
        return customProtect.send_from_directory('.', '.env', mimetype='text/plain')
    except Exception:
        return "File not found", 404

customProtect.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000
# customProtect.config['PREFERRED_URL_SCHEME'] = 'http' # Remove this line as we've set the secure flag in the config
# customProtect.config['REMEMBER_COOKIE_SAMESITE'] = 'None' # Remove this line as we've set it to 'Strict'
customProtect.config['REMEMBER_COOKIE_SECURE'] = True
# customProtect.config['REMEMBER_COOKIE_DURATION'] = 60 # Remove this line and use a secure session instead
app = customProtect
if __name__ == '__main__':
    # No rate limiting implemented on the app
    app.run(host='0.0.0.0', port=3001, debug=True)
