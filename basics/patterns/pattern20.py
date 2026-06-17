def pattern(num):
    for i in range(1, num):
        print("*"*i, end="")
        spaces = 2*(num-i)
        print(" "*spaces, end= "")
        print("*"*i,end="")
        print()
    for i in range(num,0,-1):
        print("*"*i, end ="")
        spaces = 2*(num-i)
        print(" "*spaces, end="")
        print("*"*i, end="")
        print()
num= int(input())
pattern(num)