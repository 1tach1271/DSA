def pattern(num):
    for i in range(1, num+1):
        for j in range(i):
            print(chr(65+j), end=" ")
        print()
num = 5
pattern(num)