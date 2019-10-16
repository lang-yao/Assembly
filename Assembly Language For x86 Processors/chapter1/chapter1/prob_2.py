# coding="utf-8"
'''
十六进制转十进制
'''
import math
import sys
def prob_2():
    str_bin = input("hex str: ")
    str_bin = str_bin[::-1][:32]
    number = 0
    hex = {    
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15,
    }
    for i,n in zip(str_bin, range(len(str_bin))):
        if i != '0':
            number = number + pow(16,n) * hex[i]
    print(number)

def main():
    prob_1()

if __name__ == "__main__":
    sys.exit(int(main() or 0))

