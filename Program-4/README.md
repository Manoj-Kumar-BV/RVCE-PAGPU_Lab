# Quick Start - How to Run

### Step 1: Generate Test Images

```bash
# Generate input images
python3 image_gen.py
```

This creates four test images:
- `input_512x512.png`
- `input_1024x1024.png`
- `input_2048x2048.png`
- `input_4096x4096.png`

### Step 2: Compile and Execute

```bash
# Compile
gcc -fopenmp Image_omp.c -o program4 -lgd

# Execute
./program4
```

---

## Program Objectives

**a) Demonstrate the performance of different scheduling techniques for varying chunk values**
- Compare Default, Static, Dynamic, and Guided scheduling policies
- Use chunk size of 10 for fair comparison across all scheduling types

**b) Analyze the scheduling patterns by assigning a single color value for each thread**
- Thread 0: Red tint
- Thread 1: Green tint  
- Thread 2: Blue tint
- Other threads: Pure grayscale
- Visual inspection of output images shows which thread processed which columns

---

