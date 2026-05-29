# Linux Python CS Practice

Linux、Python、Git/GitHub、C言語、コンピュータサイエンス基礎を、実装・測定・説明を通して学習するためのリポジトリです。

このリポジトリでは、ただコードを書くのではなく、以下の流れを重視しています。

```text
コードを書く
↓
実行して結果を見る
↓
処理時間や挙動を測定する
↓
CPU・メモリ・OS・コンパイラなどのCS基礎と結び付けて説明する
↓
Git/GitHubで記録する
```

## 目的

1年間で、情報系の基礎知識と実装経験を結び付け、長期インターンや就職活動で説明できる実務的な力を身につけることを目的にしています。

特に意識していることは以下です。

- Linux / WSL の基本操作
- Git / GitHub による変更履歴管理
- Pythonによる小さな実装
- C言語によるメモリ・配列・コンパイルの理解
- 処理時間の測定
- コンパイラ最適化
- プロファイリングとボトルネック分析
- NumPyによるベクトル化の入口
- multiprocessingによる並列処理
- 学んだことをREADMEに説明として残すこと

## 学習Unit一覧

| Unit | テーマ | 主なファイル | 学んだ主な内容 |
|---:|---|---|---|
| 1 | Linux / Git 初期設定 | `README.md` | WSL、シェル、Git commit |
| 2 | Python電卓 | `calc.py` | `input()`、`int()`、変数、四則演算 |
| 3 | Pythonエラー / Markdown | `README.md` | 構文エラー、Markdown、基本コマンド |
| 4 | 電卓の改善 | `calc.py` | `if`、`elif`、`else`、0除算 |
| 5 | ファイルI/Oとログ保存 | `calc.py`, `history.txt` | ファイル書き込み、ログ、ストレージ |
| 6 | ベンチマーク入門 | `bench_test.py` | 経過時間、`time.perf_counter()` |
| 7 | メモリ階層・キャッシュ | `memory_bench_test.py` | メモリ、キャッシュ、逐次アクセス |
| 8 | 分岐とbranch prediction | `branch_bench_test.py` | if文、分岐、制御フロー |
| 9 | C言語とメモリ | `array_sum.c` | 配列、アドレス、コンパイル |
| 10 | コンパイラ最適化 | `array_sum.c` | `gcc -O0`、`gcc -O2`、warning |
| 11 | プロファイリング | `profile_test.py` | profiling、bottleneck、測定による改善 |
| 12 | SIMD / ベクトル化 | `vector_test.py` | NumPy ndarray、vectorization、SIMDの入口 |
| 13 | マルチコア / multiprocessing | `multiprocessing_test.py` | process、CPUコア、overhead、並列処理 |

## 学んだこと

### 1. 測定してから改善する

プログラムが速いか遅いかを感覚で判断するのではなく、`time.perf_counter()` やCの `clock()` を使って処理時間を測定しました。

測定した例:

- Pythonのループ処理
- C言語の `-O0` と `-O2` の比較
- 関数ごとのprofiling
- Python for文とNumPyの比較
- single process と multi process の比較

### 2. PythonとCの実行方式の違い

Pythonでは、`.py` ファイルをCPUが直接実行しているわけではなく、`python3` がコードを読みながら実行します。

```bash
python3 bench_test.py
```

C言語では、`.c` ファイルをそのまま実行するのではなく、`gcc` で実行ファイルを作ってから実行します。

```bash
gcc array_sum.c -o array_sum
./array_sum
```

この違いから、単純な大量ループではCの方が速くなりやすいことを確認しました。

### 3. メモリ上のデータの持ち方

Pythonのlist、Cの配列、NumPy配列の違いを学びました。

Python list:

```text
[参照][参照][参照]
  ↓     ↓     ↓
 PyInt PyInt PyInt
```

C配列 / NumPyの数値配列:

```text
[数値][数値][数値]
```

Python listは柔軟ですが、数値計算では管理コストが大きくなりやすいです。  
一方、C配列やNumPyの `int64` 配列では、同じ型の数値データが連続して並ぶため、大量データ処理に向いています。

### 4. 並列処理は必ず速いわけではない

`multiprocessing` を使い、single process と multi process の処理時間を比較しました。

小さい処理では、プロセスを作る・仕事を分ける・結果を集めるといった `overhead` により、multi processの方が遅くなる場合がありました。

一方、大きい処理では、複数コアで処理を分担する効果が出て、multi processの方が速くなる場合がありました。

## 実行方法

Pythonの例:

```bash
python3 bench_test.py
python3 memory_bench_test.py
python3 branch_bench_test.py
python3 profile_test.py
python3 vector_test.py
python3 multiprocessing_test.py
```

C言語の例:

```bash
gcc array_sum.c -o array_sum
./array_sum
```

コンパイラ最適化の比較:

```bash
gcc -O0 array_sum.c -o array_sum_O0
gcc -O2 array_sum.c -o array_sum_O2
./array_sum_O0
./array_sum_O2
```

## 必要ライブラリ

Pythonの外部ライブラリは `requirements.txt` に記録しています。

インストール:

```bash
python3 -m pip install -r requirements.txt
```

現在使用している主なライブラリ:

```text
numpy
```

## Git / GitHubでの管理方針

ソースコードと学習ログはGitで管理します。

一方、コンパイルで生成される実行ファイルや、環境ごとに作られるファイルは `.gitignore` で除外します。

除外している例:

- `array_sum`
- `array_sum_O0`
- `array_sum_O2`
- `.venv/`
- `__pycache__/`

## 現在の到達地点

Unit 13まで完了しています。

現在理解した主な内容:

- Linux / WSLでの開発操作
- Git/GitHubによる履歴管理
- Pythonの基本文法
- ファイルI/Oとログ保存
- ベンチマーク
- メモリ階層とキャッシュの入口
- 分岐と制御フロー
- C言語の配列とアドレス
- コンパイラ最適化
- profilingとbottleneck
- NumPyによるベクトル化
- multiprocessingによる並列処理

## 今後の予定

- Unit 14: 総復習・説明化
- Unit 15: ミニOS開発の準備
- QEMUを使った小さいOS実験
- HTTP / API / DB
- Docker
- AI APIの活用

## 関連成果物

学習支援Webアプリ「Focus Grove」も開発・公開しています。

```text
https://focus-grove.onrender.com/login
```
