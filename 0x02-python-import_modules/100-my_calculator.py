#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    if (len(sys.argv) - 1) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("1")

    else:
        a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

        a, b = int(a), int(b)
        if operator == '+':
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
            print("0")
        elif operator == '-':
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
            print("0")
        elif operator == '*':
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
            print("0")
        elif operator == '/':
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
            print("0")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            print("1")
