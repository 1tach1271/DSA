def pattern(num):
    if num == 0:
        print(0)
    a = [0,1]
    for i in range (2,num+1):
        a.append(a[i-1] +a[i-2])
    return a 
num = int(input("Enter the number:- "))
print(pattern(num))