def count_vowels(user_input):
    vowels = ['A', 'E', 'I', 'O','U']
    print(type(vowels))
    count = 0
    for i in user_input:
        if i.upper() in vowels:
            count = count + 1
    return count

user_input = input("Enter the input:")
real_count = count_vowels(user_input)
print(real_count)