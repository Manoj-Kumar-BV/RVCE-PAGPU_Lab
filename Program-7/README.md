# Program 7: Matrix Multiplication using OpenACC

This program demonstrates matrix multiplication using OpenACC directives for potential GPU acceleration. The program compares performance between OpenACC-accelerated and standard CPU implementations.

## Quick Start - How to Run

### Compile and Execute (CPU Version)

```bash
# Compile with GCC (runs on CPU)
gcc -fopenmp mat_mul.c -o program7

# Execute
./program7
```

---

## Program Objective

Implement matrix multiplication (C = A × B) using:
- **OpenACC directives** for GPU acceleration (when GPU compiler available)
- **Standard CPU implementation** for verification
- **Performance comparison** between accelerated and CPU versions

---