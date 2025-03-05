n = int(input("Enter a number: "))
count = 0 
temp = abs(n) 
while temp > 0:
    temp //= 10
    count += 1  
if n == 0: 
    count = 1
print(f"The number {n} has {count} digits.")
