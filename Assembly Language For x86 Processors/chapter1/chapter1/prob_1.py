# coding="utf-8"
import math
import sys
def prob_1():
    str_bin = input("binary str: ")
    str_bin = str_bin[::-1]
    number = 0
    for i,n in zip(str_bin, range(len(str_bin))):
        if i != '0':
            number = number + pow(2,n)
    print(number)

def main():
    prob_1()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
