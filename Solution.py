# def f(n):
#     for i in range(n):
#         for j in range(i+1):
#             print(chr(65+i),end=" ")
#         print()
# n = int(input())
# f(n)

# def f(n):
#     a=0
#     b=0
#     while n>0:
#         b=n%10
#         a+=1
#         n=n//10
#     print(a)
# n=int(input())
# f(n)

# def f(arr):
#     arr[:]=arr[::-1]
#     print(arr)

# arr=list(map(int,input().split()))
# f(arr)

# from collections import defaultdict
# def f(arr,n):
#     h = defaultdict(int)
#     for i in range(n):
#         h[arr[i]]+=1
#     maxc=0
#     minc=n 
#     maxe=0
#     mine=0
#     for a,b in h.items():
#         if b>maxc:
#             maxc=b
#             maxe=a 
#         if b<minc:
#             minc=b
#             mine=a
#     print(maxe,mine)

# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# def f(arr,n):
#     for i in range(0,n-1):
#         a=i
#         for j in range(i+1,n):
#             if arr[a]>arr[j]:
#                 a=j
#         arr[i],arr[a]=arr[a],arr[i]
#     print(arr)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

# def f(arr,n,k):
#     a=0
#     left=0
#     right=0
#     s=arr[0]
#     while right<n:
#         while left<=right and  s>k:
#             s-=arr[left]
#             left+=1
#         if s==k:
#             a=max(a,right-left+1)
#         right+=1
#         if right<n:
#             s+=arr[right]
#     print(a)
# arr=list(map(int,input().split()))
# n=len(arr)
# k=int(input())
# f(arr,n,k)

# def f(arr,n):
#     m=float('-inf')
#     s=0
#     start=0
#     anss=-1
#     anse=-1
#     for i in range(n):
#         if s==0:
#             start=i
#         s+=arr[i]
#         if s>m:
#             m=s
#             anss=start
#             anse=i
#         if s<0:
#             s=0
#     print(m)
#     for i in range(anss,anse+1):
#         print(arr[i],end=" ")

# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)

