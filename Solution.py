# 1.
# def f(n):
#     for i in range(n):
#         for j in range(i+1):
#             print(chr(65+i), end=" ")
#         print()
# n=int(input())
# f(n)

# 2.
# def f(n):
#     l=0
#     m=0
#     while n>0:
#         l=n%10
#         m=m*10+l
#         n=n//10
#     print(m)
# n=int(input())
# f(n)

# 3.
# def f(n):
#     if n <=1:
#         return 0
#     a=[]
#     a.append(0)
#     a.append(1)
#     print(a[0])
#     print(a[1])
#     for i in range(2,n+1):
#         b=a[i-2]+a[i-1]
#         a.append(b)
#     for i in range(n+1):
#         print(a[i],end=" ")
# n=int(input())
# f(n)

# 4.
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

# 5.
# def m(arr,low,high):
#     if low>=high:
#         return
#     mid=(high+low)//2
#     m(arr,low,mid)
#     m(arr,mid+1,high)
#     ms(arr,low,mid,high)
# def ms(arr,low,mid,high):
#     a=[]
#     left=low
#     right=mid+1
#     while left<=mid and right<=high:
#         if arr[left]<=arr[right]:
#             a.append(arr[left])
#             left+=1
#         else:
#             a.append(arr[right])
#             right+=1
#     while left<=mid:
#         a.append(arr[left])
#         left+=1
#     while right<=high:
#         a.append(arr[right])
#         right+=1
#     for i in range(low,high+1):
#         arr[i]=a[i-low]
# arr=list(map(int,input().split()))
# n=len(arr)
# m(arr,0,n-1)
# print(arr)

# 6.
# def f(arr,n,k):
#     l=0
#     left=0
#     right=0
#     sum=arr[0]
#     while right<n:
#         while left<= right and sum>k:
#             sum-=arr[left]
#             left+=1
#         if sum==k:
#             l =max(l,right-left+1)
#         right+=1
#         if right<n:
#             sum+= arr[right]
#     print(l)
# arr=list(map(int, input().split()))
# n=len(arr)
# k=int(input())
# f(arr,n,k)

# 7.
# def f(arr,n):
#     a=[]
#     for i in range(n):
#         b=True
#         for j in range(i+1,n):
#             if arr[i]<arr[j]:
#                 b=False
#                 break
#         if b:
#             a.append(arr[i])
#     print(a)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

