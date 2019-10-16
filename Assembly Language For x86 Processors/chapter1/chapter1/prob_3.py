# coding="utf-8"
'''
十进制转二进制
'''
import sys

def prob_3():
    num = int(input("num: "))
    bin_str = ""
    while num != 0:
            ms = num % 2
            num = num // 2
            bin_str += str(ms)
    print(bin_str[::-1])

def main():
    prob_3()

if __name__ == "__main__":
    sys.exit(int(main() or 0))