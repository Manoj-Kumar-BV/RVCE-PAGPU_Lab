# Program 2: Parallel Matrix Multiplication using OpenMP

This program demonstrates parallel matrix multiplication using OpenMP with various optimization techniques including loop collapsing, SIMD vectorization, and different thread counts.

## Quick Start - How to Run

### Compile and Execute

```bash
# Compile
gcc -fopenmp matrix_multiply.c -o program2

# Execute
./program2
```

---

## Overview

This program performs matrix multiplication (A × B = C) where all matrices are square matrices of the same size. It benchmarks the performance across different matrix sizes and thread counts to demonstrate the benefits of parallel computing.

**Matrix Multiplication Formula**: 
```
C[i][j] = Σ(A[i][k] × B[k][j]) for k = 0 to n-1
```

---

## File Description

- **matrix_multiply.c** - OpenMP implementation of parallel matrix multiplication
- **program2** - Compiled executable

---

## Algorithm Details

### Matrix Multiplication Process

1. **Memory Allocation**: Dynamically allocates three matrices (matrix1, matrix2, result)
2. **Initialization**: Fills matrices with random values (0-99) using parallel loops
3. **Multiplication**: Performs matrix multiplication using nested loops
4. **Benchmarking**: Tests performance with 1, 2, 4, and 8 threads
5. **Cleanup**: Frees allocated memory to prevent memory leaks

### OpenMP Optimization Techniques Used

1. **`#pragma omp parallel for`** - Parallelizes loop iterations across threads
2. **`collapse(2)`** - Combines two nested loops into a single iteration space for better load balancing
3. **`schedule(static)`** - Distributes loop iterations uniformly among threads
4. **`#pragma omp simd`** - Enables SIMD (Single Instruction Multiple Data) vectorization for better CPU utilization
5. **`reduction(+:sum)`** - Ensures thread-safe summation by creating private copies and merging results

---

## Test Configuration

### Matrix Sizes Tested
- 100 × 100 (10,000 elements)
- 400 × 400 (160,000 elements)
- 1600 × 1600 (2,560,000 elements)
- 3200 × 3200 (10,240,000 elements)

### Thread Counts Tested
- 1 thread (sequential baseline)
- 2 threads
- 4 threads
- 8 threads

---

## Expected Output Format

```
+------------+------------+------------+------------+------------+
| MatrixSize |   1 Thread |   2 Thread |   4 Thread |   8 Thread |
+------------+------------+------------+------------+------------+
|        100 |   0.000123 |   0.000089 |   0.000067 |   0.000056 |
|        400 |   0.012345 |   0.006789 |   0.003456 |   0.002123 |
|       1600 |   0.789012 |   0.456789 |   0.234567 |   0.123456 |
|       3200 |   6.543210 |   3.456789 |   1.789012 |   0.987654 |
+------------+------------+------------+------------+------------+
```

*Note: Times shown are examples in seconds. Actual values will vary based on your hardware.*

---

## Performance Analysis

### Expected Observations

1. **Execution Time**: Decreases as thread count increases (up to the number of physical cores)
2. **Speedup**: Calculated as `Time(1 thread) / Time(N threads)`
3. **Efficiency**: May decrease with more threads due to overhead and synchronization
4. **Scalability**: Larger matrices benefit more from parallelization

### Typical Speedup Patterns

- **Small matrices (100×100)**: Limited speedup due to overhead dominating computation
- **Medium matrices (400×400, 1600×1600)**: Good speedup with 2-4 threads
- **Large matrices (3200×3200)**: Best speedup, near-linear scaling up to physical core count

### Diminishing Returns

Adding more threads than physical CPU cores may result in:
- Minimal performance improvement
- Possible performance degradation due to context switching
- Increased memory bandwidth contention

---

## Compilation Details

### Compiler Command
```bash
gcc -fopenmp matrix_multiply.c -o program2
```

### Compiler Flags
- **`-fopenmp`** - Enables OpenMP support in GCC
- **`-o program2`** - Specifies output executable name

### Optional Optimization Flags
```bash
# For better performance (recommended)
gcc -fopenmp -O3 matrix_multiply.c -o program2

# With additional optimizations
gcc -fopenmp -O3 -march=native matrix_multiply.c -o program2
```

**Flag Explanations:**
- **`-O3`** - Enables aggressive compiler optimizations
- **`-march=native`** - Optimizes for the specific CPU architecture

---

## Memory Management

### Dynamic Memory Allocation
- Uses `malloc()` to allocate memory for matrices at runtime
- Allows testing different matrix sizes without recompilation
- Memory size = `rows × cols × sizeof(int) × 3 matrices`

### Memory Requirements by Matrix Size
- 100×100: ~0.12 MB
- 400×400: ~1.9 MB
- 1600×1600: ~30.5 MB
- 3200×3200: ~122 MB

### Memory Cleanup
- All dynamically allocated memory is freed after computation
- Prevents memory leaks and allows multiple test runs

---

## How to Analyze Results

### Calculate Speedup
```
Speedup = Time(1 thread) / Time(N threads)
```

Example: If 1 thread takes 8 seconds and 4 threads take 2 seconds:
```
Speedup = 8 / 2 = 4×
```

### Calculate Efficiency
```
Efficiency = Speedup / Number of threads × 100%
```

Example: With 4× speedup on 4 threads:
```
Efficiency = 4 / 4 × 100% = 100%
```

### Ideal vs. Real Performance
- **Ideal Speedup**: Linear (2 threads = 2× faster, 4 threads = 4× faster)
- **Real Speedup**: Sub-linear due to:
  - Thread creation/synchronization overhead
  - Memory bandwidth limitations
  - Cache coherence overhead
  - Load imbalance

---

## Prerequisites

### Required Software
```bash
# Install GCC with OpenMP support (usually pre-installed)
sudo apt-get install gcc

# Verify OpenMP support
gcc --version
```

### System Requirements
- Multi-core processor (recommended: 4+ cores)
- Sufficient RAM (at least 512 MB free for largest matrix)
- Linux/Unix environment with GCC 4.2 or later

---

## Troubleshooting

### Common Issues

1. **Compilation Error: "omp.h not found"**
   ```bash
   # Install build-essential package
   sudo apt-get install build-essential
   ```

2. **Slow Performance with Many Threads**
   - Check your CPU core count: `nproc`
   - Don't use more threads than physical cores
   - Consider hyperthreading limitations

3. **Segmentation Fault**
   - Usually caused by insufficient memory
   - Try smaller matrix sizes first
   - Check available memory: `free -h`

4. **No Performance Improvement**
   - Verify OpenMP is enabled: add `printf("Threads: %d\n", omp_get_max_threads());`
   - Check if running in single-threaded mode
   - Ensure `-fopenmp` flag is used during compilation

---

## Learning Objectives

1. Understand parallel matrix multiplication algorithms
2. Learn OpenMP parallelization directives and clauses
3. Analyze parallel performance and speedup
4. Explore optimization techniques (loop collapsing, SIMD)
5. Understand memory management in C
6. Evaluate efficiency vs. thread count trade-offs
7. Recognize Amdahl's Law limitations in parallel computing

---

## Advanced Topics

### OpenMP Directives Used

| Directive | Purpose |
|-----------|---------|
| `#pragma omp parallel for` | Distributes loop iterations across threads |
| `collapse(2)` | Merges nested loops for better parallelization |
| `schedule(static)` | Assigns equal chunks of iterations to threads |
| `#pragma omp simd` | Vectorizes inner loop using SIMD instructions |
| `reduction(+:sum)` | Safely accumulates sum across threads |

### Performance Tuning Tips

1. **Matrix Size**: Larger matrices benefit more from parallelization
2. **Thread Count**: Match to physical core count for best results
3. **Schedule Type**: Try `dynamic` or `guided` for irregular workloads
4. **Chunk Size**: Experiment with `schedule(static, chunk_size)`
5. **NUMA Awareness**: Use `numactl` for multi-socket systems

---

## References

- [OpenMP Official Documentation](https://www.openmp.org/)
- [GCC OpenMP Support](https://gcc.gnu.org/onlinedocs/libgomp/)
- Matrix Multiplication Complexity: O(n³)

---

## Author Information

**Course:** RVCE - Parallel Algorithms on GPU Lab  
**Program:** Program 2 - Parallel Matrix Multiplication  
**Implementation:** OpenMP with SIMD Optimization
