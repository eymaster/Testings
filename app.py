from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, World!</h1><p>This is a simple website using Python and Flask.</p>"

if __name__ == "__main__":
    app.run()
