def s(arr,n,a):
    for i in range(n):
        if arr[i]==a:
            return i
    return -1


arr=list(map(int, input().split()))
n = len(arr)
a = int(input())
print(s(arr,n,a))