# Quick Start - How to Run

### Compile and Execute

```bash
# Compile
mpicc mpi_msg.c -o program5

# Execute with 4 processes (recommended)
mpirun -np 4 ./program5

# Can also run with 2-6 processes
mpirun -np 5 ./program5
```

---

## Program Objective

**Write an MPI program with 4 processes where:**
- Process 1 sends "Hello" to Process 0
- Process 2 sends "CSE" to Process 0
- Process 3 sends "RVCE" to Process 0
- Process 0 receives and displays all messages

---
