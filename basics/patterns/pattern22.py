def pattern(num):
    for i in range(2*num-1):
        for j in range(2*num-1):
            top = i
            left = j
            right = (2*num-2)-j
            bottom = (2*num-2)-i
            print(num-min(top,left,right,bottom),end=" ")
        print()
num = int(input())
pattern(num)