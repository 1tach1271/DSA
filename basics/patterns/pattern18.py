def pattern(num):
    for i in range(num):
        for j in range(i):
            print(chr(65+num+j-i),end="")
        print()
num = int(input())
pattern(num)