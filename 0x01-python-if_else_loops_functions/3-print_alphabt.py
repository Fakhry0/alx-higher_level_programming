#!/usr/bin/python3

for char in range(ord('a'), ord('z')+1):
    if char == ord('q') or char == ord('e'):
        pass
    else:
        print("{}" .format(chr(char)), end="")
