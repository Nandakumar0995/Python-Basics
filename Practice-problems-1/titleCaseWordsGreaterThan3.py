input_text = ['hi', 'hello', 'welcome', 'no', 'yes']
# second_input = []
# def string_greater_than_three(input_text):
#     for i in (input_text):
#         if(len(i)>3):
#             second_input.append(i.title())
#     return(second_input)

# result = string_greater_than_three(input_text)
# print(f'Title Greater Than Three:{result}')
#----------------------------------------------------------------------------------------
# def string_greater_than_three(input_text):
#     return len(input_text)>3

# def return_as_title(input_text):
#     return input_text.title()

# print(list(map(return_as_title,filter(string_greater_than_three, input_text))))
#----------------------------------------------------------------------------------------
num = list(map (lambda value: value.title(),filter(lambda value:len(value)>3, input_text)))
print(num)


print(list(
    map(lambda value: value.title(),
        filter(lambda value: len(value)> 3, input_text))))