"""
Fermat Near Miss Finder - Version 1

This program searches for near misses of Fermat's Last Theorem:
x^n + y^n ≈ z^n  for n > 2

The user provides:
- n: exponent (3 <= n <= 11)
- k: upper bound for x and y (k > 10)

The program checks all pairs (x, y) in [10, k], finds the closest z,
and computes the miss and relative miss.

Author: Rishitha Musunuru && Jyothi Swaroop Kumar Jammula
"""

import math

def main():
    # Request exponent n
    n = int(input("Enter the value of n (2 < n < 12): "))
    if n <= 2 or n >= 12:
        print("Invalid input. n must be between 2 and 12.")
        return

    # Request upper bound k
    k = int(input("Enter the value of k (k > 10): "))
    if k <= 10:
        print("Invalid input. k must be greater than 10.")
        return

    # Variables to track the best (smallest) relative miss
    smallest_relative_miss = float("inf")
    best_x = best_y = best_z = 0
    best_miss = 0

    # Iterate over all pairs (x, y)
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            total = math.pow(x, n) + math.pow(y, n)

            # Closest z approximation
            z = round(total ** (1.0 / n))

            # Compute candidate misses
            miss1 = abs(total - math.pow(z, n))
            miss2 = abs(total - math.pow(z + 1, n))

            # Choose the smaller miss
            if miss1 <= miss2:
                miss = miss1
                chosen_z = z
            else:
                miss = miss2
                chosen_z = z + 1

            # Relative miss
            relative_miss = miss / total

            # Print details for this case
            print(f"x: {x}, y: {y}, z: {chosen_z}, Miss: {miss:.0f}, Relative Miss: {relative_miss:.7f}")

            # Update best result
            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best_x, best_y, best_z, best_miss = x, y, chosen_z, miss

    # Final result
    print("\nSmallest Relative Miss Found:")
    print(f"x: {best_x}, y: {best_y}, z: {best_z}, Miss: {best_miss:.0f}, Relative Miss: {smallest_relative_miss:.7f}")


if __name__ == "__main__":
    main()
