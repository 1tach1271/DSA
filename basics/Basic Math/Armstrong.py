def pattern(num):
    c=len(str(num))
    a=0
    n=num
    while n>0:
        last_digit = n%10
        a= last_digit**c + a
        n=n//10
    if a ==num:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
num = int(input())
pattern(num)