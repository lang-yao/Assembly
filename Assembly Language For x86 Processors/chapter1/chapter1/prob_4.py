# coding="utf-8"
'''
十进制转十六进制
'''
import sys

def prob_3():
    num = int(input("num: "))
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
    print(bin_str[::-1])

def main():
    prob_3()

if __name__ == "__main__":
    sys.exit(int(main() or 0))