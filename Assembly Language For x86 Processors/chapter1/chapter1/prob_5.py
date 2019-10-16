# coding=utf-8
import sys
global b
def num_to_btype(num, b):
    str_num = ""
    while num != 0 :
        str_num += str(num % b)
        num = num // b

    return str_num[::-1]

def btype_to_num(bt ,b):
    num1 = 0
    bt = bt[::-1]

    for i,n in zip(bt, range(len(bt))):
        num1 = num1 + int(i) * pow(b, n)

    return num1

def main():
    global b
    b = int(input("b: "))
    num1 = btype_to_num(input("first num: "), b)
    num2 = btype_to_num(input("second num: "), b)
    print(num1, num2)
    print(num_to_btype(num1 + num2, b))

    return 0

if __name__ == "__main__":
    sys.exit(int(main() or 0))