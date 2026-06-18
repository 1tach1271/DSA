def pattern(num):
    print("*"*num,end="")
    print()
    for i in range(num-2):
        print("*",end="")
        spaces=num-2
        print(" "*spaces,end="")
        print("*",end="")
        print()
    print("*"*num,end="")
    print()
num = int(input())
pattern(num)