user_input = input("Enter your text: ")
count =""
for i in range(len(user_input)):
    if (user_input.count(user_input[i])==1):
        count = count + user_input[i]
    else:
        print(f"greater than once:{user_input[i]} ")

print(count[0])

