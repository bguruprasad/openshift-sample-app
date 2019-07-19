import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome"

@app.route("/how are you")
def hellp():
    return "I am doing great, Thanks for asking"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8080)