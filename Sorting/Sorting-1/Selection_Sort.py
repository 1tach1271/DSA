def selection_sort(arr,n):
    for i in range(0,n-1):
        a = i
        for j in range(i+1,n):
            if arr[j]<arr[a]:
                a = j
        arr[i],arr[a]=arr[a],arr[i]
    print(arr)
arr = list(map(int, input("Enter the array ").split()))
n = len(arr)
selection_sort(arr,n)