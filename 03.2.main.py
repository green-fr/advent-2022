# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

alphabet = '.' + ''.join(chr(i) for i in range(ord('a'), ord('z') + 1)) + ''.join(chr(i) for i in range(ord('A'), ord('Z') + 1))

def check_one_pack(three_lines):
    for char in three_lines[0]:
        if (char in three_lines[1]):
            if (char in three_lines[2]):
                return alphabet.index(char)


with open('03.input.txt', 'r') as file:
    counter = 0;
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        three_lines = lines[i : i + 3]
        counter += check_one_pack(three_lines)
    print(counter)
