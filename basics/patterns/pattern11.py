def pattern(num):
    for i in range(num):
        if i%2==0:
            val = 1
        else:
            val = 0
        for j in range(i+1):
            print(val, end = "")
            val = 1-val
        print()
num= int(input())
pattern(num)