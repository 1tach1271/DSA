def pattern( num):
        rev = 0
        while num > 0:
            lastDigit = num % 10
            rev = rev * 10 + lastDigit
            num = num // 10
        return rev
num = int(input())
print(pattern(num))