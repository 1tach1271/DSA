def p(arr,n):
    i =0
    s=set()
    for j in range(n):
        s.add(arr[i])
        i+=1
    print(s)

arr = list(map(int,input().split()))
n = len(arr)
p(arr,n)