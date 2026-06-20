def pattern(num):
    for i in range(1,num+1):
        if num%i ==0:
            print(i,end=",")
num = int(input())
pattern(num)