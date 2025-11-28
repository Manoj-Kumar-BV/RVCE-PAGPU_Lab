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

