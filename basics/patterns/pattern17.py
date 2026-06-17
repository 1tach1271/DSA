def pattern(num):
    for i in range(num):
        spaces = num-i
        print(" "*spaces,end="")
        for j in range(i):
            print(chr(65+j), end="")
        for j in range(i,-1,-1):
            print(chr(65+j), end="")
        print()
num = int(input())
pattern(num)

