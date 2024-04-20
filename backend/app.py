from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/api/healthchecker", methods=["GET"])
def healthchecker():
    return {"status": "success", "message": "Integrate Flask Framework with Next.js"}


if __name__ == "__main__":
    app.run(debug=True)
