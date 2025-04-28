from flask import Flask, jsonify


app = Flask(__name__)


@app.root_path("/")
def home():
    []
    return jsonify({"message": "!Hola desde flask en Docker!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




