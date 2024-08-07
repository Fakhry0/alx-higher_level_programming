#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    if (len(sys.argv) - 1) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    else:
        a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

        a, b = int(a), int(b)
        if operator == '+':
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif operator == '-':
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif operator == '*':
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif operator == '/':
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
