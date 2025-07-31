input_text = int(input("Enter your input:"))
fibonacci= []
a, b = 0, 1
for _ in range(input_text):
        fibonacci.append(b)
        temp = a + b
        a = b
        b = temp
print(fibonacci)
