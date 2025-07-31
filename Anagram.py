import itertools
import nltk
from nltk.corpus import words

valid_anagrams =set()

def anagram_generator(input_text):

    permutation = set(itertools.permutations(input_text)) # with the input, finding the permustations and looping to convert the set{'c','a','t'} to set "cat" using join
    dictionar = set(words.words()) # saving 2lakhs of words from words library
    
    for p in dictionar:  
        if(p in permutation and p != input_text ):         # checking expected and actual or not equal also given input combination is available in dict
            valid_anagrams.add(p)
    return valid_anagrams

input_text = input("Enter your input: ").lower()

while(not input_text.isalpha()):
    input_text = input("Enter your input: ").lower()

result = anagram_generator(input_text)

if  result:
    print(f"Given word {input_text} is Anagram, becasue we got {result}")
else:
    print(f"Given {input_text} is not Anagram")
