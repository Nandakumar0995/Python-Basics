from datetime import datetime

user_input = input("Enter you DOB:")
right_input = user_input.split("/")
user_birth_year = int(right_input[2])
user_birth_month = int(right_input[1])
user_birth_date = int(right_input[0])

current_year = datetime.now().year
current_month = datetime.now().month
current_date = datetime.now().day

year = current_year - user_birth_year 
if ((user_birth_month > current_month) or (user_birth_month == current_month and user_birth_date > current_date)):
    year = year -1

print("your age is", year)

