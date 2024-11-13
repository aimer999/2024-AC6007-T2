from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return "Hello, Flask!"

# 启动服务器
if __name__ == '__main__':
    app.run(debug=True)