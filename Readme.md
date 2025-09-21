# Fermat Near Miss Finder (Python Version 1)

## What does this program do?
This program looks for **near misses** of Fermat's Last Theorem. The theorem says:

```
x^n + y^n = z^n   has no integer solutions for n > 2
```

Our program doesn't try to disprove it, but instead finds cases where `x^n + y^n` comes very close to `z^n`.

## How to Get the Code
1. Clone the repository (or download files directly):  
   ```bash
   git clone https://github.com/MusunuruRishitha/SE-Assignment-1
   cd SE-Assignment-1
   ```
2. Make sure the file `fermat_near_miss_v1.py` is inside your project folder.

## How to Run
Run the program using Python 3:
```bash
python fermat_near_miss_v1.py
```
Then provide inputs when prompted:
- Exponent n (between 3 and 11)
- Upper bound k (> 10)

## Example Run
```
Enter the value of n (2 < n < 12): 3
Enter the value of k (k > 10): 20
x: 10, y: 10, z: 14, Miss: 4, Relative Miss: 0.0001830
...
Smallest Relative Miss Found:
x: 10, y: 10, z: 14, Miss: 4, Relative Miss: 0.0001830
```

## Requirements
- Python 3 installed.
- No extra libraries required.

## Notes
- Larger values of k take longer to compute.
- Floating-point math may cause very small rounding differences.
