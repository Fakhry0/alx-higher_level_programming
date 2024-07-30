#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    
    i = len(sys.argv) - 1

    if i == 0:
        print("{} argument.".format(i))
    elif i == 1:
        print("{} argumment:".format(i))
        print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(i))
        for _ in range(i):
            print("{}: {}".format(_+1, sys.argv[_+1]))
