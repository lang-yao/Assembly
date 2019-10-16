# coding="utf-8"
'''
第一章1.7.2算法基础习题
'''
from prob_1 import *
from prob_2 import *
from prob_3 import *
import sys

def hello():
    print('i am hello')

def main(fun):
    globals()["prob_" + fun]()
    return 0

if __name__ == "__main__":
    #fun_name = int(input("problem id:"))
    fun_name = '2'
    sys.exit(int(main(fun_name) or 0))
