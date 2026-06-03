from flask import Flask, request, jsonify
import sqlite3 
from datetime import datetime

##アプリ本体作成
app = Flask(__name__)

DB_NAME = "study_logs.db"

def get_conn():
    ##データ接続
    conn = sqlite3.connect(DB_NAME)
    ##セレクトした結果を辞書みたいにして扱いやすくする。
    ##row["id"] row["title"] row["minutes"] こんなかんじ
    conn.row_factory = sqlite3.Row
    return conn 

def def_db():
    conn = get_conn()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            minutes INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

##POSTリクエスト
@app.route("/study-logs", methods=["POST"])
def post_study_log():
    ##POSTにおけるHTTPリクエストのボディーに入ってるJSONをパイソンの辞書に変換する
    data = request.get_json()
    ##エラーチェック
    if data is None:
        return jsonify({
            "error": "JSON body is required"
        }), 400

    title = data.get("title")
    minutes = data.get("minutes")

    if title is None or minutes is None:
        return jsonify({
            "error": "title and minutes are required"
        }), 400
    ##数値変換（数字のみの制約？？に見える）
    try:
        minutes = int(minutes)
    except (ValueError, TypeError):
        return jsonify({
            "error": "minutes must be an integer"
        }), 400

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO study_logs (title, minutes, created_at)
        VALUES (?, ?, ?)
    """, (title, minutes, created_at))

    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
##更新した値の確認
    return jsonify({
        "id": new_id,
        "title": title,
        "minutes": minutes,
        "created_at": created_at
    }), 201

@app.route("/study-logs", methods=["GET"])
def get_study_logs():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, minutes, created_at
        FROM study_logs
        ORDER BY id DESC
    """)
    ##セレクトの中身を代入
    rows = cursor.fetchall()
    conn.close()

    logs = []

    for row in rows:
        logs.append({
            "id": row["id"],
            "title": row["title"],
            "minutes": row["minutes"],
            "created_at": row["created_at"]
        })

    return jsonify({
        "logs": logs
    })
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
##jsonから足し算するAPI
@app.route("/add-json", methods=["POST"])
def add_json():
    ##POSTの中のボディのJSONをpythonのディクショナリとして受け取る
    data = request.get_json()

    if data is None:
        return jsonify({
            "error": "JSON body is required"
        }), 400

    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({
            "error": "a and b are required"
        }), 400

    try:
        a = int(a)
        b = int(b)
    except (ValueError, TypeError):
        return jsonify({
            "error": "a and b must be integers"
        }), 400

    result = a + b

    return jsonify({
        "a": a,
        "b": b,
        "result": result
    })

if __name__ == "__main__":
    def_db()
    app.run(host="127.0.0.1", port=5000, debug=True)
