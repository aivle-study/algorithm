def prime_number(number):   
    if number != 1:                 
        for f in range(2, number):  
            if number % f == 0:     
                return False    
    else:                        
        return False            
    return True   
input_integer = int(input())
integer_list = (x for x in range(2, input_integer + 1))
prime_numbers = []
for num in integer_list:
    if prime_number(num):
        prime_numbers.append(num)
for i in range(len(prime_numbers)):
    if input_integer%prime_numbers[i]==0:
        if prime_number(int(input_integer/prime_numbers[i])):
            print(prime_numbers[i],int(input_integer/prime_numbers[i]))
            break
        else:
            print("IMPOSSIBLE")
            break