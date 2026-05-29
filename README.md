# linux-python-practice

start date : 2026-5-26

## Goal

Linux,GIT,python,web,API,DB,Dockerを１年で実務レベルに引き上げる。

## Today

* WSL/Ubuntuを確認した
* Linuxの基本コマンドを触った
* 学習用フォルダを作った

## Commands

* pwd
* ls
* cd
* mkdir

## Day 2

* calc.py を作った
* Pythonで足し算を実行した
* input() で入力を受け取った
* int() で文字列を数値に変換した

## Python notes

* print() は画面に表示する
* input() はキーボード入力を受け取る
* int() は文字列を整数に変換する

## Day 3

* calc.py の入力表示を改善した
* +, -, \*, / を選べるようにした
* if / elif / else を使った
* git diff でcommit前の変更内容を確認した

## Python notes

* if は条件分岐に使う
* elif は追加の条件に使う
* else はどの条件にも当てはまらない場合に使う

## Day 4

* calc.py を四則演算に対応させた
* if / elif / else で条件分岐を使った
* 0で割る場合の処理を追加した
* git diff でcommit前の変更を確認した
* input() で受け取った文字列を int() で数値に変換する流れを確認した

## Architecture notes

* input() の値は最初は文字列
* int() によって文字列が数値に変換される
* if文は条件によってプログラムの流れを変える
* 足し算や引き算はCPU内部ではALUが担当する
* 変数の値はメモリ上に保持される

## Day 6

* bench\_test.py を作成した
* time.perf\_counter() で処理時間を測った
* n=1000000 のとき約0.04秒だった
* n=10000000 のとき約0.24〜0.29秒だった
* 入力値が大きくなると、ループ回数が増えて処理時間も増えることを確認した

## Day 7

* memory\_bench\_test.py を作成した
* 1からnまでの数字をリストとしてメモリ上に作成した
* そのリストを順番に読みながら合計した
* time.perf\_counter() を使って、合計処理にかかる時間を測定した
* n=1,000,000 のとき約0.017秒だった
* n=10,000,000 のとき約0.210秒だった

## Day 9

* array\_sum.c を作成した
* C言語で配列の合計を計算した
* gccでCコードをコンパイルした
* 配列要素のアドレスを表示した
* Cの配列は同じ型の値がメモリ上に連続して並ぶことを学んだ

Pythonでは、listは主にオブジェクトへの参照を並べている。
一方、C言語の配列では、同じ型の値がメモリ上に連続して並ぶ。
Pythonのlist:
\[参照]\[参照]\[参照]\[参照]\[参照]
↓     ↓     ↓     ↓     ↓
1     2     3     4     5

Cのint配列:
\[1]\[2]\[3]\[4]\[5]

\## Day 10



\- C言語の `array\_sum.c` を使って、実行時間を測定した

\- `gcc -O0` と `gcc -O2` でコンパイルし、実行時間を比較した

\- 同じCコードでも、コンパイラ最適化によって実行時間が変わることを確認した

\- PythonとCの実行方式の違いを学んだ

\- `scanf` の戻り値を無視している warning を観察した

\- warning を入力チェックに活かすことで、安全性・堅牢性の向上につながることを学んだ



\## Result



| N | C `-O0` | C `-O2` |

|---:|---:|---:|

| 1,000,000 | 0.003738秒 | 0.000748秒 |

| 10,000,000 | 0.040035秒 | 0.007263秒 |

Pythonでは、`.py` ファイルをCPUが直接実行しているわけじゃない。

## Day 11

## Day 11

- profile_test.py を作成した
- 処理を make_num(), sum_num(), sum_without_list() に分けた
- time.perf_counter() で処理ごとの実行時間を測定した
- リスト作成ありの合計処理と、リストを作らず直接合計する処理を比較した
- profiling によって、どの処理が時間を使っているかを確認した
- bottleneck の考え方を学んだ

## Result

| N | make_numbers | sum_numbers | sum_without_list | total |
|---:|---:|---:|---:|---:|
| 1,000,000 | 0.043秒 | 0.017秒 | 0.021秒 | 0.081秒 |
| 10,000,000 | 0.246秒 | 0.194秒 | 0.220秒 | 0.660秒 |

## CS Connection

### Profiling

Profilingは、プログラムのどの部分が時間を使っているかを調べること。

全体の実行時間だけを見ると、どこが遅いのか分からない。

今回のコードでは、以下の処理を分けて測定した。

```python
make_num()
sum_num()
sum_without_list()
## Day 12

- `vector_test.py` を作成した
- Pythonのfor文による合計処理と、NumPyによる合計処理を比較した
- NumPy ndarray と Python list の違いを学んだ
- NumPyの `int64` 配列では、Python intオブジェクトへの参照ではなく、数値データが連続して並ぶことを学んだ
- SIMD / vectorization の入口を学んだ

## Result

| N | Python for | NumPy |
|---:|---:|---:|
| 100,000 | 0.00713秒 | 0.00386秒 |
| 10,000,000 | 0.29464秒 | 0.04107秒 |

## CS Connection

### SIMD

SIMDは `Single Instruction, Multiple Data` の略である。

1つの命令で複数のデータをまとめて処理する考え方であり、数値計算や配列処理で性能向上につながる。

今回の実験だけで、NumPyが必ずSIMDを使ったと断定することはできない。  
しかし、Pythonのfor文で1個ずつ処理する場合と、NumPyのような最適化された配列処理では、実行時間に大きな差が出ることを確認できた。

### Vectorization

Vectorizationは、1つずつ処理するループを、配列やベクトル単位でまとめて処理できる形にすること。

Pythonのfor文では、Pythonインタプリタが1回ずつ処理するため、大量ループでは遅くなりやすい。

一方、NumPyは内部でC言語などによる高速な実装を使っており、連続した数値データを効率よく処理できる。

### Python list and NumPy ndarray

Pythonのlistは、主にPythonオブジェクトへの参照を並べている。

一方、今回のNumPy配列は `dtype=np.int64` を指定しており、`int64` の数値データが連続したメモリ領域に並ぶ。

```text
Python list:
[参照][参照][参照][参照]
  ↓     ↓     ↓     ↓
 PyInt PyInt PyInt PyInt
## Day 13

- multiprocessingを使って、single processとmulti processの実行時間を比較した
- CPUコア数を `os.cpu_count()` で確認した
- workers数を入力し、使用するプロセス数を変えて測定した
- 小さい処理では並列化のoverheadにより遅くなる場合があることを確認した
- 大きい処理ではmulti processの方が速くなる場合があることを確認した

## Result

| N | workers | single | multi |
|---:|---:|---:|---:|
| 1,000,000 | 4 | 0.037秒 | 0.123秒 |
| 1,000,000 | 10 | 0.047秒 | 0.047秒 |
| 10,000,000 | 4 | 0.233秒 | 0.125秒 |
| 10,000,000 | 10 | 0.225秒 | 0.098秒 |

## CS Connection

### Multiprocessing

Multiprocessingは、複数のプロセスを使って処理を分担する方法である。

現代のCPUには複数のコアがあるため、処理を分割できれば、複数コアで同時に進められる可能性がある。

今回のPCでは、`os.cpu_count()` によりCPU数が12であることを確認した。

### Overhead

Overheadは、目的の処理そのもの以外に追加でかかるコストである。

multi processでは、以下のようなoverheadがある。

- プロセスを作る
- 処理範囲を分ける
- 各プロセスに仕事を渡す
- 結果を集める
- 最後に合計する
- OSがプロセスを管理する

N=1,000,000では処理本体が軽く、overheadの影響でmulti processが遅くなる場合があった。

一方、N=10,000,000では処理本体が重くなり、multi processの方が速くなった。

### Scaling

workers数を増やしても、速度がそのまま比例して上がるとは限らない。

今回、workers=10でもsingle processの10倍速にはならなかった。

これは、並列化にはoverheadがあり、CPUコア数、メモリアクセス、OSのスケジューリング、Pythonのmultiprocessingの管理コストなどが影響するためである。

### Practical meaning

実務では、並列化すれば必ず速くなるわけではない。

処理本体が十分に重く、分割しやすく、結果を集めるコストが小さい場合に、並列処理の効果が出やすい。

そのため、並列化する前後で必ず測定する必要がある。
