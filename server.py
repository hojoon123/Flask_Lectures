from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'

app.run(port=5001, debug=True)