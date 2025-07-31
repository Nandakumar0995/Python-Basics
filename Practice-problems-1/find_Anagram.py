from collections import Counter

input_first_word =input("Enter your input: ").lower().replace(" ","")
input_second_word =input("Enter your input: ").lower().replace(" ","")

first = Counter(input_first_word)
second = Counter(input_second_word)

if (first == second):
    print(f'Anagram {input_first_word}, {input_second_word}')
else:
    print(f'both not anagram{input_first_word}, {input_second_word}')
