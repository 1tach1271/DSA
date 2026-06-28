def pattern(arr,n):
    if n<2:
        return -1
    a = arr[0]
    b = arr[0]
    a1 = arr[0]
    b1 = arr[0]
    for i in range(0,n):
        if a < arr[i]:
            a=arr[i]
        if b > arr[i]:
            b=arr[i]
    for i in range(0,n):
        if a1< arr[i] and arr[i]!=a:
            a1 = arr[i]
        if b1 > arr[i] and arr[i]!=b:
            b1 = arr[i]
    print(f"The second largest number is {a1} and the second smallest number is {b1}")

arr = list(map(int, input("Enter the array ").split()))
pattern(arr, len(arr))        