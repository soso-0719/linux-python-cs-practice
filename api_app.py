from flask import Flask, request, jsonify
##アプリ本体作成
app = Flask(__name__)

##サーバー生きてるか確認
@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })

##関数が実行されるか確認
@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello, API"
    })

##
@app.route("/add")
def add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
##URL参照で値を受けとっている。
    result = a + b

    return jsonify({
        "a": a,
        "b": b,
        "result": result
    })

##サーバー起動　このファイルを起動したら最初にする処理。
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
