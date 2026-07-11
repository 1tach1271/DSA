# def f(n):
#     a=1
#     for i in range(n):
#         for j in range(i+1):
#             print(a,end=" ")
#             a+=1
#         print()
# n = int(input())
# f(n)

# def f(n):
#     a=n
#     c=len(str(n))
#     l=0
#     m=0
#     while a>0:
#         l= a%10
#         m +=l**c
#         a=a//10
#     if m==n:
#         print("Yes")
#     else:
#         print("No")
# n=int(input())
# f(n)

# def f(n):
#     if n<=1:
#         return n
#     l=f(n-1)
#     sl=f(n-2)
#     return l+sl
# n=int(input())
# for i in range(n+1):
#     print(f(i),end=" ")

# from collections import defaultdict
# def f(arr,n):
#     h=defaultdict(int)
#     for i in range(n):
#         h[arr[i]]+=1
#     for a,b in h.items():
#         print(a,b)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# def f(arr,low,high):
#     if low<high:
#         p = pa(arr,low,high)
#         f(arr,low,p-1)
#         f(arr,p+1,high)
# def pa(arr,low,high):
#     pivot = arr[low]
#     i=low
#     j=high
#     while i<j:
#         while i<=high and arr[i]<=pivot:
#             i+=1
#         while j>=low and arr[j]> pivot:
#             j-=1
#         if i<j:
#             arr[i],arr[j]=arr[j],arr[i]
#     arr[low],arr[j]=arr[j],arr[low]
#     return j
# arr = list(map(int,input().split()))
# n=len(arr)
# f(arr,0,n-1)
# print(arr)

# def f(arr,n):
#     for i in range(n-2):
#         if arr[i]>arr[i+1]:
#             return False
#     return True
# arr = list(map(int,input().split()))
# n=len(arr)
# print(f(arr,n))

# def f(arr,n):
#     a=[]
#     b=[]
#     for i in range(n):
#         if arr[i]<0:
#             b.append(arr[i])
#         else:
#             a.append(arr[i])
#     for i in range(n//2):
#         arr[i*2]=a[i]
#         arr[2*i +1] = b[i]
#     print(arr)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# def f(arr,n):
#     a=[0]*n
#     b=0
#     c=1
#     for i in range(n):
#         if arr[i]<0:
#             a[c]=arr[i]
#             c+=2
#         else:
#             a[b]=arr[i]
#             b+=2
#     return a
# arr=list(map(int,input().split()))
# n=len(arr)
# print(f(arr,n))