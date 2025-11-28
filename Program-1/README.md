# Program 1: Monte Carlo Method for Estimating Pi

This folder contains parallel implementations of the Monte Carlo method to estimate the value of Pi (π) using statistical sampling techniques.

## Quick Start - How to Run

### 1. MPI Program
```bash
# Compile
mpicc PI_MPI.c -o program1mpi

# Execute with 4 processes
mpirun -np 4 ./program1mpi
```

### 2. OpenMP Program
```bash
# Compile
gcc -fopenmp PI_OpenMP.c -o program1openmp

# Execute
./program1openmp
```

---
