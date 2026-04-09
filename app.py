from flask import Flask, render_template, request, session, redirect, url_for, jsonify, send_from_directory, make_response
import sqlite3
import os

app = Flask(__name__)
app.headers['X-Frame-Options'] = 'SAMEORIGIN'
app.headers['X-XSS-Protection'] = '1; mode=block'
app.headers['Content-Security-Policy'] = 'upgrade-insecure-requests'

DB_PATH = 'shopeasy.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Other code here remains the same