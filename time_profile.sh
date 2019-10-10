kernprof -l compare_algs.py

python -m line_profiler compare_algs.py.lprof | tee compare_algs_profiling.txt

cmd /k