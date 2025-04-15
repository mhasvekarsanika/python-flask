from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, DevOps World!</h1><p>This is a static web page using Python Flask.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
