import sqlite3
import os
import functools

DB_PATH = 'shopeasy.db'

def require_admin_role(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # For demonstration purposes, this will be a hardcoded admin role
        if kwargs.get('user_id') == 1:
            return func(*args, **kwargs)
        else:
            raise Exception('Admin role required')
    return wrapper

def setup_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Create tables
    c.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            internal_notes TEXT
        )
    ''')
    
    c.execute('''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            image_url TEXT
        )
    ''')
    
    c.execute('''
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            card_last4 TEXT NOT NULL,
            total REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    
    c.execute('''
        CREATE TABLE user_roles (
            user_id INTEGER,
            role TEXT NOT NULL
        )
    ''')
    
    # Populate Users (10 users) with their roles
    users = [
        (1, "admin", "Alice Smith", "alice@example.com", "password123", "VIP Customer"),
        (2, "admin", "Bob Jones", "bob@example.com", "password123", "Frequent returns"),
        (3, "admin", "Charlie Brown", "charlie@example.com", "password123", "Regular"),
        (4, "admin", "Diana Prince", "diana@example.com", "password123", "High value cart limit"),
        (5, "admin", "Eve Adams", "eve@example.com", "password123", "Loyalty program"),
        (6, "admin", "Frank Castle", "frank@example.com", "password123", "Watchlist"),
        (7, "admin", "Grace Hopper", "grace@example.com", "password123", "Tech Lead"),
        (8, "admin", "Henry Ford", "henry@example.com", "password123", "Bulk ordering"),
        (9, "admin", "Ivy Carter", "ivy@example.com", "password123", "Standard"),
        (10, "admin", "Jack Sparrow", "jack@example.com", "password123", "Flagged for fraud")
    ]
    c.executemany('INSERT INTO users (id, role, name, email, password, internal_notes) VALUES (?, ?, ?, ?, ?, ?)', users)

    users = [
        (1, "admin", "Alice Smith", "alice@example.com", "password123", "VIP Customer"),
        (2, "admin", "Bob Jones", "bob@example.com", "password123", "Frequent returns"),
        (3, "admin", "Charlie Brown", "charlie@example.com", "password123", "Regular"),
        (4, "admin", "Diana Prince", "diana@example.com", "password123", "High value cart limit"),
        (5, "admin", "Eve Adams", "eve@example.com", "password123", "Loyalty program"),
        (6, "admin", "Frank Castle", "frank@example.com", "password123", "Watchlist"),
        (7, "admin", "Grace Hopper", "grace@example.com", "password123", "Tech Lead"),
        (8, "admin", "Henry Ford", "henry@example.com", "password123", "Bulk ordering"),
        (9, "admin", "Ivy Carter", "ivy@example.com", "password123", "Standard"),
        (10, "admin", "Jack Sparrow", "jack@example.com", "password123", "Flagged for fraud")
    ]
    roles = [
        (1, "admin"),
        (2, "admin"),
        (3, "admin"),
        (4, "admin"),
        (5, "admin"),
        (6, "admin"),
        (7, "admin"),
        (8, "admin"),
        (9, "admin"),
        (10, "admin")
    ]
    c.executemany('INSERT INTO user_roles (user_id, role) VALUES (?, ?)', roles)
    
    # Populate Products (5 products)
    products = [
        ("Wireless Noise-Canceling Headphones", "Premium sound with 30-hour battery life", 299.99, "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&auto=format&fit=crop&q=60"),
        ("Smart Watch Series 8", "Track your health and fitness effortlessly", 399.99, "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500&auto=format&fit=crop&q=60"),
        ("4K Ultra HD Smart TV", "55-inch display with vibrant colors", 499.99, "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500&auto=format&fit=crop&q=60"),
        ("Mechanical Gaming Keyboard", "RGB backlit with tactile switches", 129.99, "https://images.unsplash.com/photo-1595225476474-87563907a212?w=500&auto=format&fit=crop&q=60"),
        ("Ultra-Light Laptop", "16GB RAM, 512GB SSD, all-day battery", 1199.99, "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500&auto=format&fit=crop&q=60")
    ]
    c.executemany('INSERT INTO products (name, description, price, image_url) VALUES (?, ?, ?, ?)', products)
    
    # Populate Orders
    @require_admin_role
    def populate_orders(c):
        orders = [
            (1, "Alice Smith", "alice@example.com", "123 Elm St, NY", "4242", 299.99),
            (2, "Bob Jones", "bob@example.com", "456 Oak Ave, CA", "1111", 399.99),
            (3, "Charlie Brown", "charlie@example.com", "789 Pine Rd, TX", "9999", 129.99),
            (1, "Alice Smith", "alice@example.com", "123 Elm St, NY", "4242", 1199.99),
            (5, "Eve Adams", "eve@example.com", "321 Cedar Ln, WA", "8888", 499.99)
        ]
        c.executemany('INSERT INTO orders (user_id, name, email, address, card_last4, total) VALUES (?, ?, ?, ?, ?, ?)', orders)
    
    conn.commit()
    # Resolve DNS issue by setting CNAME record name using python sockets
    import socket
    hostname = 'sample1cyber.onrender.com'
    mydomain = 'namansaini2709-sample1cyber.default.onrender.com'
    myip = '127.0.0.1'
    # Create an AF_INET socket and bind it to mydomain with IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((mydomain, 0))
    s.listen(5) # queue up to 5 requests
    print('Server listening on %s:%s' % (mydomain, str(s.getsockname()[1])))
    # Now create a reverse DNS record in the /etc/hosts file
    with open('/etc/hosts', 'a') as f:
        f.write(myip + ' ' + mydomain)
    
    conn.close()
    print("Database initialised successfully.")

if __name__ == '__main__':
    setup_db()