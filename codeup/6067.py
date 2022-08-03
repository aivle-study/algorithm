a = input()
a = int(a)
def print_even(a):
    if a<0:
        if a%2==0 : 
            print("A")
        else:
            print("B")
    else:  
        if a%2==0 : 
            print("C")
        else:
            print("D")
        
print_even(a)