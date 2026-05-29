# Linux Python CS Practice

Practical learning logs and small experiments for Linux, Python, Git/GitHub, C language, and computer science fundamentals.

This repository is built as a record of hands-on study: writing code, measuring behavior, debugging errors, explaining the result, and pushing progress to GitHub.

## Purpose

The goal of this repository is to connect implementation experience with computer science fundamentals.

Main focus:

- Linux / WSL operation
- Git and GitHub workflow
- Python programming
- C language and memory
- Performance measurement
- Compiler optimization
- Profiling and bottleneck analysis
- NumPy / vectorized computation
- Multiprocessing and parallel execution

## Learning Units

| Unit | Topic | Main files | Main concepts |
|---:|---|---|---|
| 1 | Linux / Git setup | `README.md` | WSL, shell commands, Git commit |
| 2 | Python calculator | `calc.py` | `input()`, `int()`, variables, arithmetic |
| 3 | Python errors / Markdown | `README.md` | syntax errors, Markdown, command practice |
| 4 | Calculator improvement | `calc.py` | `if`, `elif`, `else`, division by zero |
| 5 | File I/O and logging | `calc.py`, `history.txt` | file writing, logs, storage |
| 6 | Benchmarking basics | `bench_test.py` | elapsed time, `time.perf_counter()` |
| 7 | Memory benchmark | `memory_bench_test.py` | memory hierarchy, cache intuition |
| 8 | Branch benchmark | `branch_bench_test.py` | branch, branch prediction, control flow |
| 9 | C array and memory | `array_sum.c` | arrays, addresses, compile and execute |
| 10 | Compiler optimization | `array_sum.c` | `gcc -O0`, `gcc -O2`, warnings |
| 11 | Profiling | `profile_test.py` | profiling, bottleneck, measurement-driven improvement |
| 12 | Vectorization / NumPy | `vector_test.py` | NumPy ndarray, vectorization, SIMD intuition |
| 13 | Multiprocessing | `multiprocessing_test.py` | process, CPU cores, overhead, parallelism |

## What I Learned

### Measurement Before Optimization

I practiced measuring execution time before guessing performance problems.

Examples:

- Python loop benchmark
- C `-O0` vs `-O2` comparison
- profiling by function
- NumPy vs Python loop comparison
- single process vs multi process comparison

### Python And C Execution Models

Python code is executed by the Python interpreter, while C code is compiled into an executable file before running.

Python:

```bash
python3 bench_test.py
```

C:

```bash
gcc array_sum.c -o array_sum
./array_sum
```

This helped me understand why C can be much faster for simple tight loops, and why optimized libraries such as NumPy are important in Python.

### Memory And Data Layout

I compared Python lists, C arrays, and NumPy arrays.

Python list:

```text
[reference][reference][reference]
     |          |          |
   PyInt      PyInt      PyInt
```

C / NumPy numeric array:

```text
[number][number][number]
```

This is important for understanding performance, cache behavior, and vectorized computation.

### Parallelism Is Not Always Faster

In the multiprocessing experiment, small workloads became slower because of overhead.

For larger workloads, multiprocessing became faster.

This showed that parallel execution must be measured, not assumed.

## How To Run

Python examples:

```bash
python3 bench_test.py
python3 memory_bench_test.py
python3 branch_bench_test.py
python3 profile_test.py
python3 vector_test.py
python3 multiprocessing_test.py
```

C examples:

```bash
gcc array_sum.c -o array_sum
./array_sum
```

Compiler optimization comparison:

```bash
gcc -O0 array_sum.c -o array_sum_O0
gcc -O2 array_sum.c -o array_sum_O2
./array_sum_O0
./array_sum_O2
```

## Requirements

Python dependencies are listed in `requirements.txt`.

Install them with:

```bash
python3 -m pip install -r requirements.txt
```

Current dependency:

```text
numpy
```

## Git / GitHub Policy

Source code and learning notes are tracked.

Generated files are ignored by `.gitignore`.

Examples of ignored files:

- C executables such as `array_sum`, `array_sum_O0`, `array_sum_O2`
- Python cache files such as `__pycache__/`
- local virtual environments such as `.venv/`

## Current Status

Completed through Unit 13:

- benchmarking
- memory and cache intuition
- branch behavior
- C arrays and addresses
- compiler optimization
- profiling
- NumPy vectorization
- multiprocessing

## Next Topics

- Unit 14: review and explanation practice
- Unit 15: mini OS preparation
- QEMU experiment
- HTTP / API / database
- Docker
- AI API integration

## Related Portfolio

I also developed and deployed a learning support web application:

Focus Grove:

```text
https://focus-grove.onrender.com/login
```
