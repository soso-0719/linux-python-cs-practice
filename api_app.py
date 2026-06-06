from flask import Flask, request, jsonify
import sqlite3 
from datetime import datetime
from flask_cors import CORS
##アプリ本体作成
app = Flask(__name__)
CORS(app, origins=[
    "http://localhost:3000",
    "http://127.0.0.1:3000"
])
DB_NAME = "study_logs.db"
##関数コーナー
def get_conn():
    ##データ接続
    conn = sqlite3.connect(DB_NAME)
    ##セレクトした結果を辞書みたいにして扱いやすくする。
    ##row["id"] row["title"] row["minutes"] こんなかんじ
    conn.row_factory = sqlite3.Row
    return conn 

def init_db():
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


def create_log(title, minutes, created_at):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO study_logs (title, minutes, created_at)
        VALUES (?, ?, ?)
    """, (title, minutes, created_at))

    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return new_id


def get_all_logs():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, minutes, created_at
        FROM study_logs
        ORDER BY id DESC
    """)

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

    return logs


def get_summary():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COUNT(*) AS total_logs,
            COALESCE(SUM(minutes), 0) AS total_minutes,
            COALESCE(AVG(minutes), 0) AS average_minutes
        FROM study_logs
    """)

    row = cursor.fetchone()
    conn.close()

    return {
        "total_logs": row["total_logs"],
        "total_minutes": row["total_minutes"],
        "average_minutes": row["average_minutes"]
    }

##関数コーナー終了
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
    
    title = str(title).strip()##前後の空白を消す

    if title == "":
        return jsonify({
        "error": "title must not be empty"
    }), 400

    ##数値変換（数字のみの制約？？に見える）
    try:
        minutes = int(minutes)
    except (ValueError, TypeError):
        return jsonify({
            "error": "minutes must be an integer"
        }), 400
    
    if minutes <= 0:
        return jsonify({
        "error": "minutes must be greater than 0"
    }), 400

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ## INSERTもここでしてる。
    new_id = create_log(title, minutes, created_at)

##更新した値の確認
    return jsonify({
        "id": new_id,
        "title": title,
        "minutes": minutes,
        "created_at": created_at
    }), 201

@app.route("/study-logs", methods=["GET"])
def get_study_logs():
    ##logsはdict
    logs = get_all_logs()
    return jsonify({
        "logs": logs
    })

@app.route("/study-logs/<int:log_id>", methods=["DELETE"])
def delete_study_log(log_id):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM study_logs
        WHERE id = ?
    """, (log_id,))
## Whereマジ大事
    conn.commit()
    deleted_count = cursor.rowcount
    conn.close()

    if deleted_count == 0:
        return jsonify({
            "error": "study log not found"
        }), 404

    return jsonify({
        "message": "study log deleted",
        "id": log_id
    })

@app.route("/study-logs/summary", methods=["GET"])
def get_study_logs_summary():
    summary = get_summary()
    return jsonify({
        "summary":summary
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
    data = request.get_json(silent=True)
    ## silent = True でHTMLの標準エラーじゃなくて自分のJSONエラーにできるらしい

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
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=True)
