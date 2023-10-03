#!/usr/bin/python3

"""
    The N queens puzzle
    placing N non-attacking queens on an N×N chessboard
"""

import sys

args = sys.argv

if len(args) != 2:
    print("Usage: nqueens N")
    exit(1)
N = int(args[1])
if not isinstance(N, int):
    print("N must be a number")
    exit(1)
if (N < 4):
    print("N must be at least 4")
    exit(1)
final = []
for i in range(N):
    running = []
    for j in range(1, N, N-2):
        running.append([i, j])
    final.extend(running)
    final.append("\n")
print(final)
