def reverse_the_number(value):
    print('reverse the number')
    result =''
    while value > 0:
        last_value = value % 10 #4
        value = int(value/10) 
        result = result + str(last_value) 
    return result

def reverse_the_string(value):
    print('reverse the string')
    value = value[::-1]
    return value

result = ''
try:
    value = input("Enter your value:")
    converted_value = int(value)
    result = reverse_the_number(converted_value)
except:
    print("Exception")
    result = reverse_the_string(value)

print("Your reversed number is {}".format(result))





