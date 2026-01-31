from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/data')
def data():
    token = request.headers.get("Authorization")
    if token != "Bearer securetoken123":
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"data": "Sensitive server data"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
