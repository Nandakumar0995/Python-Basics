value = [1, "hello", 3, "42", 7, "world"]

def integer_seperator(input_text):
    return isinstance(input_text, int)

def double_int(input_text):
    return (input_text*2)

filtered_values = list(filter(integer_seperator, value))
doubled_values = list(map(double_int, filtered_values))

# doubled_values_2  = list(map(lambda input_text: input_text*2, filter(lambda input_text:isinstance(input_text, int), value)))
print(doubled_values_2)
