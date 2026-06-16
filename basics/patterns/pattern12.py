
def pattern(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j, end="")
        spaces = 2*(num-i)
        print(" "*spaces, end ="")
        for j in range(i, 0,-1):
            print(j, end="")
        print()
num = int(input())
pattern(num)