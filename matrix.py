import numpy as np, threading, time

# Normal matrix multiplication
def normal_mult(A, B):
    n, m = A.shape
    C = np.zeros((n, B.shape[1]))
    for i in range(n):
        for j in range(B.shape[1]):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Multithreaded: one thread per row
def row_mult(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    def work(i):
        for j in range(B.shape[1]):
            for k in range(B.shape[0]):
                C[i][j] += A[i][k] * B[k][j]
    threads = [threading.Thread(target=work, args=(i,)) for i in range(A.shape[0])]
    [t.start() for t in threads]; [t.join() for t in threads]
    return C

# Multithreaded: one thread per cell
def cell_mult(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    def work(i, j): C[i][j] = sum(A[i][k] * B[k][j] for k in range(A.shape[1]))
    threads = [threading.Thread(target=work, args=(i, j)) for i in range(A.shape[0]) for j in range(B.shape[1])]
    [t.start() for t in threads]; [t.join() for t in threads]
    return C

# Example run
A, B = np.random.randint(0,10,(200,200)), np.random.randint(0,10,(200,200))
for name, func in [("Normal", normal_mult), ("Row-threaded", row_mult), ("Cell-threaded", cell_mult)]:
    t = time.time(); func(A,B); print(f"{name}: {round(time.time()-t,4)}s")


###################################################################


1 — Short summary (1–2 lines)

The program multiplies two matrices A and B using three methods: a normal single-threaded triple loop, a multithreaded version where each row is computed by one thread, and a multithreaded version where each cell is computed by its own thread. It times each approach on random 200×200 matrices.

2 — Theory (oral style)

Matrix multiplication: C = A × B, where C[i][j] = Σ_k A[i][k] * B[k][j].

Complexity of the classic algorithm is O(n³) for n×n matrices.

Python threading uses OS threads but is limited by the Global Interpreter Lock (GIL) for CPU-bound pure-Python work, so threads may not speed up pure Python loops.

NumPy’s internal operations are implemented in C and can be parallelized; calling np.dot is typically fastest.

3 — Algorithms (what the code does)

normal_mult(A,B) — standard triple nested loops:

For each row i, for each column j, compute C[i][j] summing over k.

row_mult(A,B) — one thread per row:

Create a thread for each row i. The thread computes all C[i][*] by looping over j and k.

cell_mult(A,B) — one thread per cell:

Create a thread for every (i,j). Each thread computes a single C[i][j] by summing over k.

Each method returns matrix C; main script measures execution time for each.

4 — Key concepts & why they matter (short bullets)

Triple loop — canonical O(n³) implementation. Simple and predictable.

Threading — good for I/O or when work releases GIL; for CPU-bound Python loops it suffers due to GIL.

Thread overhead — creating/joining many threads (especially cell-threaded: n² threads) is expensive and often dominates work for moderate n.

Memory layout — good locality (row vs column) affects speed; cache misses matter.

NumPy — vectorized C routines (use A.dot(B)) are far faster than Python loops.

5 — Complexity & resource analysis

Time complexity (mathematical): O(n³) for all three (same number of scalar multiplications).

Practical runtime:

normal_mult: single-threaded Python loop — slow.

row_mult: thread creation O(n) overhead; if GIL blocked, no real speedup.

cell_mult: thread creation O(n²) overhead — extremely expensive; usually worst.

Space complexity: O(n²) for result matrix C. Additional memory for threads/stack negligible compared to n² for large n but thread objects cost RAM.

Thread-safety: updates write to distinct C[i][j], so no race conditions for correctness.


8 — 10 Viva questions + crisp answers

Q: What is the mathematical formula for matrix multiplication?
A: C[i][j] = Σ_k A[i][k] * B[k][j].

Q: What is the time complexity of naive matrix multiplication?
A: O(n³) for n×n matrices.

Q: Why did cell-threaded version perform poorly?
A: It spawns O(n²) threads, incurring huge creation/join overhead and context switching.

Q: What is the Python GIL and how does it affect threading?
A: Global Interpreter Lock ensures only one Python bytecode thread runs at a time in a process, so CPU-bound Python code cannot run threads in parallel.

Q: When can threading actually help in Python?
A: For I/O-bound tasks or when the work releases the GIL (e.g., heavy C extensions like NumPy functions).

Q: How can you achieve true parallelism for CPU tasks in Python?
A: Use multiprocessing (separate processes) or native extensions (numba, C/C++) or rely on C libraries via NumPy.

Q: Is there any risk of race conditions in row_mult & cell_mult?
A: No, because each thread writes to a unique element or unique row of matrix C.

Q: Why is np.dot usually faster than explicit loops?
A: It uses optimized C/Fortran BLAS routines and vectorized operations with better cache utilization.

Q: How would you parallelize matrix multiplication efficiently?
A: Partition the result into blocks/row chunks and use process pool or BLAS multi-threading; blocked matrix multiplication improves cache locality.

Q: What is blocking (tiling) and why is it useful?
A: Break matrices into sub-blocks so inner loops work on cache-resident blocks — reduces cache misses and speeds up multiplication.
