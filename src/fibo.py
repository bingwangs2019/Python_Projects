'''
Created on 2020年2月22日

@author: Percy
'''
#conding=UTF-8
# 斐波那契数列模块

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b,end=" ")
        a, b = b, a+b
    print()
    
#if __name__ == "__main_":

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    print(result)
if __name__ == "__main_":
    print(__name__)