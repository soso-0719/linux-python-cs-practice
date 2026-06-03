import sqlite3

##操作するデータベースの名前
DB_NAME = "study_logs.db"

##データ追加関数
def insert_log(title, minutes, created_at):
    ##接続するデータベース名
    conn = sqlite3.connect(DB_NAME)
    ##SQL操作役
    cursor = conn.cursor()

    cursor.execute(
        ##stlogのカラムにバリュー代入する
        # ?はSQLインジェクション対策
        
        """
        INSERT INTO study_logs (title, minutes, created_at)
        VALUES (?, ?, ?)
        """,
        (title, minutes, created_at)
    )

    conn.commit()
    conn.close()


def fetch_logs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, minutes, created_at FROM study_logs")
    ##この取り出した値はcursorの中にアクセス可能な状態として残る
    rows = cursor.fetchall()
    ##パイソン側へ読み込む
    conn.close()
    return rows


insert_log("Python SQLite", 200, "2026-06-03")

logs = fetch_logs()

for log in logs:
    print(log)
