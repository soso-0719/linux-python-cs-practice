# Linux Python CS Practice

このリポジトリは、Linux / Git / Python / C / CS基礎 / Flask API / SQLite / Next.js を、実際に手を動かしながら学習している記録です。

単にコードを書くことだけではなく、「なぜ動くのか」「OSやCPU、メモリ、HTTP、DBとどうつながっているのか」を自分の言葉で説明できるようになることを目的にしています。

## 学習を始めた理由

大学で情報系分野を学ぶ中で、授業で得た知識を実際の開発や就職活動で説明できる力に変えたいと考え、この学習を始めました。

特に、1年後の就職活動までに、基礎知識だけでなく、実際にコードを書き、エラーを調べ、GitHubに記録し、改善していく経験を積みたいと考えています。

このリポジトリでは、Webアプリ開発だけに閉じず、Linux、Git、Python、C言語、メモリ、コンパイラ、API、DB、React/Next.js などを横断的に学んでいます。

## 目標

- Linux / WSL の基本操作を理解する
- Git / GitHub を使って変更履歴を管理する
- Pythonで小さなプログラムを作る
- C言語を通してメモリやコンパイルを理解する
- 処理時間を測定し、性能差を説明できるようにする
- FlaskでAPIを作る
- SQLiteでデータを保存する
- Next.jsからAPIを呼び出し、画面とDBをつなげる
- 学んだ内容をREADMEやコミット履歴として残す

## 現在作っているもの

現在は、学習ログを管理する小さなWebアプリを作成しています。

構成は以下の通りです。

```text
Next.js frontend
  |
  | HTTP request
  v
Flask API
  |
  | SQL
  v
SQLite database
```

できること:

- 学習ログ一覧を表示する
- 学習ログを追加する
- 学習ログを編集する
- 学習ログを削除する
- 学習時間の合計を画面に表示する

主なファイル:

```text
api_app.py                 Flask API
frontend/app/page.tsx      Next.jsの画面
data/study_logs.db         ローカルSQLiteデータベース（Git管理対象外）
```

## 使用技術

| 分野 | 技術 |
|---|---|
| OS / 環境 | Windows, WSL, Ubuntu |
| バージョン管理 | Git, GitHub |
| Backend | Python, Flask |
| DB | SQLite |
| Frontend | Next.js, React, TypeScript |
| CS基礎 | C, gcc, NumPy, multiprocessing |
| 低レイヤ学習 | QEMU, boot sector, mini OS実験 |

## API一覧

| Method | Endpoint | 内容 |
|---|---|---|
| GET | `/health` | APIサーバーの動作確認 |
| GET | `/study-logs` | 学習ログ一覧を取得 |
| POST | `/study-logs` | 学習ログを作成 |
| PUT | `/study-logs/<id>` | 学習ログを更新 |
| DELETE | `/study-logs/<id>` | 学習ログを削除 |
| GET | `/study-logs/summary` | 学習ログの集計を取得 |

## APIの処理の流れ

学習ログを新しく作成する場合:

```text
1. Next.jsのフォームに学習内容を入力する
2. ブラウザがFlaskへPOSTリクエストを送る
3. FlaskがリクエストボディのJSONを読む
4. titleとminutesをバリデーションする
5. SQLiteにデータをINSERTする
6. FlaskがJSONを返す
7. Reactがstateを更新し、画面を再描画する
```

学習ログを編集する場合:

```text
1. Editボタンを押す
2. Reactが対象のidをeditingIdに保存する
3. フォームがAddモードからEditモードに変わる
4. Saveボタンを押す
5. ブラウザがPUTリクエストを送る
6. FlaskがSQLiteの該当行をUPDATEする
7. Reactが最新のログ一覧を再取得する
```

## 学習ログ

| Day | テーマ | 主なファイル |
|---:|---|---|
| 1 | Linux / Gitの基礎 | `README.md` |
| 2 | Python初回実行 | `practices/python_basics/calc.py` |
| 3 | Pythonの構文とMarkdown | `README.md` |
| 4 | 電卓プログラムの改善 | `practices/python_basics/calc.py` |
| 5 | ファイルI/Oと履歴保存 | `practices/python_basics/` |
| 6 | ベンチマーク入門 | `practices/performance/bench_test.py` |
| 7 | メモリ階層とキャッシュの直感 | `practices/performance/memory_bench_test.py` |
| 8 | 分岐と制御フロー | `practices/performance/branch_bench_test.py` |
| 9 | C言語の配列とメモリアドレス | `practices/c_memory/array_sum.c` |
| 10 | コンパイラ最適化 | `practices/c_memory/array_sum.c` |
| 11 | プロファイリングとボトルネック | `practices/performance/profile_test.py` |
| 12 | NumPyとベクトル化 | `practices/performance/vector_test.py` |
| 13 | multiprocessing | `practices/performance/multiprocessing_test.py` |
| 14 | 総復習と説明練習 | `README.md` |
| 15-18 | Mini OS / boot実験 | `mini_os/` |
| 19 | Flask APIの基礎 | `api_app.py` |
| 20 | SQLiteの基礎 | `data/study_logs.db`, `practices/database/db_practice.py` |
| 21 | Flask API + SQLite | `api_app.py` |
| 22 | バリデーションとエラー処理 | `api_app.py` |
| 23 | 関数分割 | `api_app.py` |
| 24 | Next.jsの導入 | `frontend/` |
| 25 | Next.jsからAPIを取得 | `frontend/app/page.tsx` |
| 26 | ReactフォームからPOST | `frontend/app/page.tsx` |
| 27 | CORSとフロント/バックエンド接続 | `api_app.py`, `page.tsx` |
| 28 | DELETE機能 | `api_app.py`, `page.tsx` |
| 29 | UPDATE機能 | `api_app.py`, `page.tsx` |
| 30 | GitHub / README整理 | `README.md` |

## 学んだこと

### Linux / Git

ディレクトリ構造、WSL上のLinuxパスとWindowsパスの関係、Gitのadd / commit / log / showによる変更履歴管理を学びました。

### Python / C / 性能

PythonとCの実行方法の違い、処理時間の測定、メモリ配置、ループ、コンパイラ最適化、NumPyによるベクトル化が性能に与える影響を学びました。

### OS / 低レイヤ

Mini OS実験を通して、プログラムが最終的には機械が読めるバイナリになり、bootloader、メモリアドレス、CPUの実行、BIOS/QEMUがつながっていることを学びました。

### Web / API / DB

ブラウザがHTTPリクエストを送り、Flaskが受け取り、SQLiteに保存し、Reactがstateを更新して画面を描き直す流れを学びました。

## 起動方法

### バックエンド

```bash
python3 api_app.py
```

バックエンドURL:

```text
http://127.0.0.1:5000
```

SQLiteのデータはローカルでは以下に保存されます。

```text
data/study_logs.db
```

### フロントエンド

```bash
cd frontend
npm run dev
```

フロントエンドURL:

```text
http://localhost:3000
```

## 必要なライブラリ

Pythonライブラリのインストール:

```bash
python3 -m pip install -r requirements.txt
```

主なライブラリ:

```text
flask
flask-cors
numpy
```

## 関連プロジェクト

学習支援Webアプリ「Focus Grove」も開発・公開しています。

```text
https://focus-grove.onrender.com/login
```

## 今後の予定

この学習リポジトリで得た知識をもとに、次はポートフォリオとして見せやすいアプリ「AI Study Grove」を開発する予定です。

AI Study Groveでは、API設計、DB操作、Reactのstate管理に加えて、AIを使った学習支援機能を組み込む予定です。

単に学習記録を保存するだけでなく、学んだ内容の振り返り、苦手ポイントの整理、復習問題の生成までできるアプリを目指します。
