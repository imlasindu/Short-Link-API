from flask import Flask, redirect, render_template, request, jsonify, json
from shortener import short


app = Flask(__name__)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
