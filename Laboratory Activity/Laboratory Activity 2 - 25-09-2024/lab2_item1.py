num = int(input("Enter an integer: "))

if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
