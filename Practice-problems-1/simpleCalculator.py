def simple_calculator(**kwargs):

    operations = kwargs['operand']
    operand1 = kwargs['operand1']
    operand2 = kwargs['operand2']

    if (operations == 'ADD'):
        return operand1 + operand2
    elif (operations == 'SUB'):
        return operand1 - operand2
    elif (operations == 'MUL'):
        return operand1 * operand2
    elif (operations == 'DIV'):
        return operand1 / operand2
    else:
        print("Invalid Input")
        return 'Invalid'

allowed_operations = ['ADD', 'SUB', 'MUL', 'DIV']

is_input_valid = False

while not is_input_valid:
    operations = input("Enter your operation: ")
    operand1 = input("Enter your operand1 input : ")
    operand2 = input("Enter your operand2 input : ")

    if(operations.upper() in allowed_operations and operand1.isdigit and operand2.isdigit ):
        is_input_valid = True

    else:
        print("Entered value is not part of operand or format")
else:
    result = simple_calculator(operand = operations.upper(), operand1=int(operand1), operand2=int(operand2) )

print(f"result is {result}")





