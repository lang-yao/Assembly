# coding=utf-8
'''
十六进制加法
'''
import sys
global b
def btype_to_num(str_bin, b):
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
    return number


def num_to_btype(num):
    bin_str = ""
    hex = {
        0:'0',
        1:'1',
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        7:'7',
        8:'8',
        9:'9',
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F',    
    }
    while num != 0:
            ms = num % 16
            num = num // 16
            bin_str += hex[ms]
    return bin_str[::-1]


def main():
    global b
    b = 16
    num1 = btype_to_num(input("first num: "), b)
    num2 = btype_to_num(input("second num: "), b)
    print(num1, num2)
    print(num_to_btype(num1 + num2))

    return 0

if __name__ == "__main__":
    sys.exit(int(main() or 0))