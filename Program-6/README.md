# Program 6: Parallel Word Search in Text Files

This program performs parallel word searching in text files using OpenMP. It searches for multiple words simultaneously across different threads and measures execution time for performance analysis.

## Quick Start - How to Run

### Compile and Execute

```bash
# Compile
gcc -fopenmp wordsearch.c -o program6

# Execute (requires 2 arguments: filename and thread count)
./program6 a_1mb.txt 4

# Test different configurations
./program6 a_1mb.txt 1    # 1 thread
./program6 a_1mb.txt 2    # 2 threads
./program6 a_1mb.txt 4    # 4 threads
./program6 a_1mb.txt 8   # 8 threads

# Test with different size files
./program6 a_2mb.txt 1     # 2mb file with 1 thread
./program6 a_10mb.txt 2    # 10mb file with 2 threads
# other different configurations.
Note: a_(size)mb given only for easy convention.
```

---

## Program Objective

**Parallel word search to demonstrate:**
- Performance improvement with multiple threads
- Speedup analysis with different file sizes
- OpenMP parallelization for I/O-bound tasks

---
