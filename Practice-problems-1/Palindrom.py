
def check_if_palindrome (user_input):
    cleaned_text = user_input.replace(" ","")
    reversed_text = cleaned_text[::-1]
    
    if(cleaned_text == reversed_text):
     print("palindrome")
    else:
     print("not palindrome")

user_input =input("Enter your input:").lower()
check_if_palindrome (user_input)

