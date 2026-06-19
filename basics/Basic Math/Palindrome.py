def pattern(num):
    rev = 0
    a=num
    while a>0:
        lastDigit = a % 10
        rev = rev * 10 + lastDigit
        a = a // 10
    if num == rev:
        print("Palindrome Number")
    else:
        print("Not Palindrome")
num = int(input())
pattern(num)