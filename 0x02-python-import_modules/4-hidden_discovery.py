#!/usr/bin/python3
import hidden_4

names = dir(hidden_4)
for each in names:
    if (each[:2] != "__"):
        print(each)
