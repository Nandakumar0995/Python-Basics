import random

def generate_number():    # generate a random number from 1-10
    return random.randint(1,10) 

generated_number = generate_number()

is_user_input_valid = False

while (not is_user_input_valid):
    user_input = input("Enter your number from 1 to 10: ") # get input from user
    
    # QUERY -> user_input.digit() - False
    # 11 / 0

    if (not user_input.isdigit() or int(user_input) <=0 or int(user_input) > 10 ):
        print(f"Enter a valid number: {user_input}")
        # is_user_input_valid = False
    else:
        is_user_input_valid = True
        
if (generated_number == int(user_input)):
    print(f"You guessed the right number: {generated_number}")     # print the number then If both are eql print success else fail 
else:
    print(f"Better luck next time, the number is: {generated_number}")





   
