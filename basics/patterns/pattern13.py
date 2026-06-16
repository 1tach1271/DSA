def pattern(num):
    count = 1
    for i in range(1,num+1):
        for j in range(1, i+1):
            print(count, end = " ")
            count= count+1
        print()
num = 5
pattern(num)