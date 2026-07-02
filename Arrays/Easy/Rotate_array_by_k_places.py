def r(arr, n, k,direction):
    if direction=="left":

        k = k % n
        temp = arr[:k]

        for i in range(k, n):
            arr[i-k] = arr[i]

        for i in range(k):
            arr[n-k+i] = temp[i]

    else:
        k =k%n
        temp=arr[n-k:]
        for i in range(n-k-1,-1,-1):
            arr[i+k]=arr[i]
        for i in range(k):
            arr[i]=temp[i]
    print(arr)


arr = list(map(int, input().split()))
n = len(arr)
k = int(input())
direction = input()
r(arr, n, k,direction)