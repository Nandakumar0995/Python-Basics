input_text = input("Enter the numbers:" )  #1,2,3,4,5
correct_number = input_text.split(',')

print(type(correct_number))
count = 0
for i in correct_number:
    count = count +1

print(count)
