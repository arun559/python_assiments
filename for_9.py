numbers = [12, 45, 78, 23, 56, 89, 34]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"The largest number in the list is: {largest}")
