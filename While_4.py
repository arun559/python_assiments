odd_even = input("Do you want to print odd or even numbers? (odd/even): ").strip().lower()
S = int(input("Enter the start number: "))
A = int(input("Enter the ending number: "))


if S >= A:
    print("limts nned to change")
else:
    if odd_even == "odd":
        if S % 2 == 0:
            S += 1
        while S <= A:
            print(S)
            S += 2
    elif odd_even == "even":
        if S % 2 != 0:
            S += 1
        while S <= A:
            print(S)
            S += 2
    else:
        print("Invalid input! Please enter 'odd' or 'even'.")



