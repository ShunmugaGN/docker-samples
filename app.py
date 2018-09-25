import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "I solemnly swear, I have no idea about Python or Flask!"

if __name__ == "__main__":
    app.run()
