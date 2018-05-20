#encouding=utf-8
from flask import Flask, jsonify, redirect, request
import pymysql

app = Flask(__name__, static_url_path='', static_folder='front')


@app.route("/")
def index():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)