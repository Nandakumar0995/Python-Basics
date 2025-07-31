input_number = int(input("Enter your number: "))

def check_isprime(input_number):
    if input_number <= 1:
        return False
    count = 0
    for i in range(2, input_number+1): # 10
        if(input_number%i == 0):    #0
            count +=1   #1
        if(count >1):
            break
        else:
            continue
    if(count >1):
        return(False)
    else:
        return(True)

result = check_isprime(input_number)
print(result)
    

        


