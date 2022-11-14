from math import factorial
def C(a,b):
    return factorial(a)//factorial(b)//factorial(a-b)

print(C(5,3))