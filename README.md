# Linux Python CS Practice

このリポジトリは、Linux / Git / Python / C / CS基礎 / Flask API / SQLite / Next.js を、実際に手を動かしながら学習している記録です。

単にコードを書くことだけではなく、「なぜ動くのか」「OSやCPU、メモリ、HTTP、DBとどうつながっているのか」を自分の言葉で説明できるようになることを目的にしています。

## Motivation

大学で情報系分野を学ぶ中で、授業で得た知識を実際の開発や就職活動で説明できる力に変えたいと考え、この学習を始めました。

特に、1年後の就職活動までに、基礎知識だけでなく、実際にコードを書き、エラーを調べ、GitHubに記録し、改善していく経験を積みたいと考えています。

このリポジトリでは、Webアプリ開発だけに閉じず、Linux、Git、Python、C言語、メモリ、コンパイラ、API、DB、React/Next.js などを横断的に学んでいます。

## Goals

- Linux / WSL の基本操作を理解する
- Git / GitHub を使って変更履歴を管理する
- Pythonで小さなプログラムを作る
- C言語を通してメモリやコンパイルを理解する
- 処理時間を測定し、性能差を説明できるようにする
- FlaskでAPIを作る
- SQLiteでデータを保存する
- Next.jsからAPIを呼び出し、画面とDBをつなげる
- 学んだ内容をREADMEやコミット履歴として残す

## Current Main App

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

Main files:

```text
api_app.py                 Flask API
frontend/app/page.tsx      Next.js page
data/study_logs.db         Local SQLite database (not committed)
```

## Tech Stack

| Area | Tools / Languages |
|---|---|
| OS / Environment | Windows, WSL, Ubuntu |
| Version Control | Git, GitHub |
| Backend | Python, Flask |
| Database | SQLite |
| Frontend | Next.js, React, TypeScript |
| CS Practice | C, gcc, NumPy, multiprocessing |
| Low-level Practice | QEMU, boot sector, simple mini OS experiment |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | API server health check |
| GET | `/study-logs` | Get all study logs |
| POST | `/study-logs` | Create a new study log |
| PUT | `/study-logs/<id>` | Update a study log |
| DELETE | `/study-logs/<id>` | Delete a study log |
| GET | `/study-logs/summary` | Get study log summary |

## Example API Flow

When a new study log is created:

```text
1. User submits a form in the Next.js frontend
2. Browser sends a POST request to Flask
3. Flask reads JSON from the request body
4. Flask validates title and minutes
5. SQLite inserts the data
6. Flask returns JSON
7. React updates state and re-renders the screen
```

When a study log is edited:

```text
1. User clicks Edit
2. React stores the target id in editingId
3. The form changes from Add mode to Edit mode
4. User clicks Save
5. Browser sends a PUT request
6. Flask updates the row in SQLite
7. React fetches the latest logs again
```

## Learning Log

| Day | Topic | Main Files |
|---:|---|---|
| 1 | Linux / Git basics | `README.md` |
| 2 | First Python program | `practices/python_basics/calc.py` |
| 3 | Python syntax and Markdown | `README.md` |
| 4 | Calculator improvement | `practices/python_basics/calc.py` |
| 5 | File I/O and history log | `practices/python_basics/` |
| 6 | Benchmark basics | `practices/performance/bench_test.py` |
| 7 | Memory hierarchy and cache intuition | `practices/performance/memory_bench_test.py` |
| 8 | Branch and control flow | `practices/performance/branch_bench_test.py` |
| 9 | C arrays and memory address | `practices/c_memory/array_sum.c` |
| 10 | Compiler optimization | `practices/c_memory/array_sum.c` |
| 11 | Profiling and bottleneck | `practices/performance/profile_test.py` |
| 12 | NumPy and vectorization | `practices/performance/vector_test.py` |
| 13 | Multiprocessing | `practices/performance/multiprocessing_test.py` |
| 14 | Review and explanation practice | `README.md` |
| 15-18 | Mini OS / boot experiment | `mini_os/` |
| 19 | Flask API basics | `api_app.py` |
| 20 | SQLite basics | `data/study_logs.db`, `practices/database/db_practice.py` |
| 21 | Flask API + SQLite | `api_app.py` |
| 22 | Validation and error handling | `api_app.py` |
| 23 | Function splitting | `api_app.py` |
| 24 | Next.js setup | `frontend/` |
| 25 | Fetch API from Next.js | `frontend/app/page.tsx` |
| 26 | Form POST from React | `frontend/app/page.tsx` |
| 27 | CORS and frontend/backend connection | `api_app.py`, `page.tsx` |
| 28 | DELETE feature | `api_app.py`, `page.tsx` |
| 29 | UPDATE feature | `api_app.py`, `page.tsx` |
| 30 | GitHub / README cleanup | `README.md` |

## What I Learned

### Linux / Git

I learned how files are managed inside directories, how WSL connects Windows and Linux paths, and how Git records changes through add, commit, log, and show.

### Python / C / Performance

I compared Python and C programs, measured execution time, and learned that implementation details such as memory layout, loops, compiler optimization, and vectorization can strongly affect performance.

### OS / Low-level Basics

Through a mini OS experiment, I learned that programs must eventually become machine-readable binary data, and that bootloaders, memory addresses, CPU execution, and BIOS/QEMU are connected.

### Web / API / DB

I learned how a browser sends HTTP requests, how Flask receives them, how SQLite stores data, and how React updates the UI through state.

## How to Run

### Backend

```bash
python3 api_app.py
```

Backend URL:

```text
http://127.0.0.1:5000
```

SQLite data is stored locally at:

```text
data/study_logs.db
```

### Frontend

```bash
cd frontend
npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

## Requirements

Install Python packages:

```bash
python3 -m pip install -r requirements.txt
```

Main packages:

```text
flask
flask-cors
numpy
```

## Related Project

I also developed and published a learning support web app called Focus Grove.

```text
https://focus-grove.onrender.com/login
```

## Next Step

After building this practice project, I plan to develop a more portfolio-oriented application: AI Study Grove.

AI Study Grove will use the knowledge from this repository, including API design, database operations, React state management, and AI-assisted learning support.

The goal is to build an application that does not only store study records, but also helps users reflect on what they learned, identify weak points, and generate review questions.
