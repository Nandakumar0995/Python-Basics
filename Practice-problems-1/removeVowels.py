input_text = ["apple", "sky", "orange", "fly"]
vowels = {'A','E','I','O','U'}
def remove_vowels_word(input):
    return  not any (i.upper() in vowels for i in input)

def to_upper(input):
    return  input.upper()

# removed_value = list(map (to_upper, filter(remove_vowels_word, input_text)))

removed_value = list(
    map(lambda value:value.upper(), 
        filter (lambda value:not any(i.upper() in vowels for i in value), input_text)))
print(removed_value)


