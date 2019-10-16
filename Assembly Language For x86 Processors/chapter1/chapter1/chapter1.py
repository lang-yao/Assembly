# coding="utf-8"

from prob_1 import *
import sys

def hello():
    print('i am hello')

def main(fun):
    globals()["prob_"+fun]()
    return 0

if __name__ == "__main__":
    #fun_name = int(input("problem id:"))
    fun_name = '1'
    sys.exit(int(main(fun_name) or 0))
