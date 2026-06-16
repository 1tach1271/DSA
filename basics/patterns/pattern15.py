def pattern(num):
    for i in range(num, 0, -1):
        for j in range(i):
            print(chr(65+j), end=" ")
        print()
num = 5
pattern(num)