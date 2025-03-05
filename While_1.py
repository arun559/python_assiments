n = int(input("Enter a number: ")) 
factorial = 1  
i = n 
steps = "" 
while i > 0: 
    factorial *= i 
    steps += str(i)  
    if i > 1:
        steps += " * "  
    i -= 1  # Decrease i by 1
print(f"{n}! = {steps} = {factorial}")
