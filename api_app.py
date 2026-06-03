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
    ##URL参照で値を受けとっている。
    a_text = request.args.get("a")
    b_text = request.args.get("b") 
    ## Noneのエラー処理
    if a_text is None or b_text is None:
        return jsonify({
            "error": "a and b are required"
        }), 400
    
    try:
        a = int(a_text)
        b = int(b_text)
    except ValueError:
        return jsonify({
            "error": "a and b must be integers"
        }), 400

    result = a + b

    return jsonify({
        "a": a,
        "b": b,
        "result": result
    })

##サーバー起動　このファイルを起動したら最初にする処理。
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
