def s(arr1,n):
    xorr=0
    for i in range(n):
        xorr=xorr^arr1[i]
    print(xorr)

arr1 = list(map(int,input().split()))
n = len(arr1)
s(arr1,n)