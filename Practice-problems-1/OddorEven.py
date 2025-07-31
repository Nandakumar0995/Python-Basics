

def odd_or_even(score):
    if  (score % 2 == 0):
        return("Even")
    else:
        return ("Odd")

score = int(input("Enter you score:"))
result = odd_or_even(score)
print("your score is {}".format(result) )