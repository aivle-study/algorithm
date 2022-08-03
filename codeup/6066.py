a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

def print_even(a):
    if a%2==0 : 
        print("even")
    else:
        print("odd")
        
print_even(a)
print_even(b)
print_even(c)