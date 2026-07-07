# def p(a,n):
#     c=0
#     b=0
#     for i in range(n):
#         if a[i]=="*":
#             c+=1
#         else:
#             b+=1
#     if c>=b:
#         print(c-b)
#     else:
#         print(b-c)
# a = input()
# n=len(a)
# p(a,n)

# def p (arr,n):
#     c=1
#     b=arr[0]
#     for i in range(1,n):
#         if arr[i]>b:
#             c+=1
#             b=arr[i]
#     print(c)
# arr = list(map(int,input().strip("{}").split(",")))
# n = len(arr)
# p(arr,n)

# from collections import defaultdict
# def p(arr,n):
#     hash=defaultdict(int)
#     for i in range(n):
#         hash[arr[i]]+=1
#     for a,b in hash.items():
#         if b%2!=0:
#             return a
#     return "All are even"
# arr=input().strip("[]").split(",")
# n = len(arr)
# print(p(arr,n))

# n = int(input())
# arr=[]
# for i in range(n):
#     arr.append(input())
# print(arr)



# def f(n,k,j,m,p):
#     c=0
#     c = m//k
#     d = p//j
#     if (m%k)>=1 :
#         a=1
#     else:
#         a=0
#     if (p%j)>=1:
#         b=1
#     else:
#         b=0
#     print(n-(c+d+max(a,b)))

# n = int(input())
# k = int(input())
# j = int(input())
# m = int(input())
# p = int(input())
# f(n,k,j,m,p)

# def k(arr,n):
#     low, mid, high = 0,0,n-1
#     while mid<=high:
#         if arr[mid]==0:
#             arr[low],arr[mid]=arr[mid],arr[low]
#             mid+=1
#             low+=1
#         elif arr[mid]==1:
#             mid+=1
#         else:
#             arr[high],arr[mid]=arr[mid],arr[high]
#             high-=1
#     print(arr)
# arr= list(map(int,input().strip("[]").split(",")))
# n=len(arr)
# k(arr,n)

# def a(arr):

# arr=input()
# import json
# def k(arr):
#     p = []
#     for chars in zip(*arr):
#         if len(set(chars))==1:
#             p.append(chars[0])
#         else:
#             break
#     print("".join(p))
# a= input()
# arr = json.loads(a)
# k(arr)

# def f(a,b):
#     days ={
#         "mon":0,
#         "tue" : 1,
#         "wed" : 2,
#         "thur": 3,
#         "fri" : 4,
#         "sat" : 5,
#         "sun" :6
#     }
#     start = days[a]

#     first_sunday = 6 - start

#     if first_sunday >= b:
#         return 0

#     return 1 + (b - first_sunday - 1) // 7
        
# a= input().lower()
# b = int(input())
# print(f(a,b))
# r=int(input())
# c=int(input())
# row=0
# m=0
# for i in range(r):
#     s = 0
#     for j in range(c):
#         s+=int(input())
#     if s >m:
#         m=s 
#         row = i+1 
# print(row)

# a = int(input())
# b = int(input())
# matrix=[]
# for i in range(a):
#     r=[]
#     for j in range(b):
#         c=int(input())
#         r.append(c)
#     matrix.append(r)
# print(matrix)
# a = int(input())
# b=int(input())
# s= ((b-a+1)*(2*a + b -1))//2
# print(s)

# def f(a,b,c):
#     if a==b==c:
#         return 0
#     if a>b and a>c:
#         for i in range(1,a):
#             d=i
#             b+=1
#             c+=1
#             a-=1
#             if a==b==c:
#                 return d
#             else:
#                 d+=1
#     if c>b and c>a:
#         for i in range(1,c):
#             d=i
#             b+=1
#             a+=1
#             c-=1
#             if a==b==c:
#                 return d
#             else:
#                 d+=1 
#     if b>a and b>c:
#         for i in range(1,b):
#             d=i
#             a+=1
#             c+=1
#             b-=1
#             if a==b==c:
#                 return d
#             else:
#                 d+=1
#     return -1
# a=int(input())
# b=int(input())
# c=int(input())
# print(f(a,b,c))

# def f(arr,n):
#     a=0
#     for i in range(n):
#         a^=arr[i]
#     print(a)

# arr = list(map(int,input().strip("[]").split(",")))
# n = len(arr)
# f(arr,n)
# def f(n):
#     if n <=1:
#         return False
#     for i in range(2,int( n**(0.5)) +1):
#         if n%i==0:
#             return False
#     return True
# def p(n):
#     count=0
#     s=0
#     a=2
#     while count<n:
#         if f(a):
#             s+=a
#             count+=1
#         a+=1
#     print(s)
# n = int(input())
# p(n)

# t = int(input())
# a={}
# e=0
# while t>0:
#     c = input()
#     if c!="done":
#         d=int(input())
#         e+=d
#         a[c]=d
#     elif c=="done":
#         break

# print("Total Income: ",t)
# print("Total expense: ",e)
# total_saving = t-e 
# print("TotalSaving: ",total_saving)
# for c,d in a.items():
#     print(c,d)
# from collections import defaultdict

# def f(a,n):
#     s=0
#     y=0
#     hash = defaultdict(int)
#     for i in range(n):
#         hash[a[i]]+=1
#     for a,b in hash.items():
#         if b>s:
#             y=a
#             s=b 
#     print(y)

    # for i in range(n):
    #     b=a[i]
    #     c=1
    #     for j in range(i+1,n):
    #         if b == a[j]:
    #             c+=1
# a = input()
# n=len(a)
# f(a,n)

# from collections import defaultdict
# def f(s):
#     if len(s) == 0:
#         print("Invalid Input")
#         return
#     freq = defaultdict(int)
#     for ch in s:
#         freq[ch] += 1
#     first_non = "None"
#     for ch in s:
#         if freq[ch] == 1:
#             first_non = ch
#             break
#     max_char = s[0]
#     max_freq = freq[s[0]]
#     for ch in s:
#         if freq[ch] > max_freq:
#             max_freq = freq[ch]
#             max_char = ch
#     print(first_non, max_char)
# a = input()
# f(a)
# def f(n,x,y,num):
#     for i in range(n):
#         print(num[i],num[i+1])
#     print()

# def g(n,x,y,m):
#     a = f(n,x,y,m)
#     for i in range(n) 

# n = int(input())
# x=int(input())
# y=int(input())
# num = list(map(int,input().strip("[]").split(",")))
# g(n,x,y,num)

# def f(n, x, y, arr):
#     count = 0

#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 num = int(str(arr[i]) + str(arr[j]))
#                 if x <= num <= y:
#                     count += 1
#     print(count)
# n = int(input())
# x=int(input())
# y=int(input())
# num = list(map(int,input().strip("[]").split(",")))
# f(n,x,y,num)
# def f(n):
#     if n <=1:
#         return False
#     for i in range(2,int( n**(0.5)) +1):
#         if n%i==0:
#             return False
#     return True
# def p(n):
#     count=0
#     s=0
#     a=2
#     while count<n:
#         if f(a):
#             s+=a
#             count+=1
#         a+=1
#     print(s)
# n = int(input())
# p(n)
# def p(num):
#     if num<=1:
#         return 
#     for i in range(2,int(num**(0.5))+1):
#         if num%i==0:
#             return False
#     return True
# def f(a):
#     m=2
#     count=0
#     while True:
#         if p(m):
#             count+=1
#             if count==a:
#                 return m
#         m+=1
        
#     print(m)

# a = int(input())
# b = int(input())
# print(f(a)*f(b)-1)

# a = list(map(int,input().split()))
# ar=set()
# b=[]
# for x in a:
#     if x not in ar:
#         ar.add(x)
#         b.append(x)
# print(b)

# def f(arr,n,k):
#     for i in range(n):
#         s=arr[i]
#         for j in range(i,n):
#             s+=arr[j]
#             if s==k:
#                 return "Yes"
#     return "No"

# arr=list(map(int,input().split()))
# n = len(arr)
# k=int(input())
# print(f(arr,n,k))

# def f(arr,n):
#     c=1
#     for i in range(1,n):
#         if arr[0]==arr[i]:
#             c+=1
#     print(n-c)

# n=int(input())
# arr= list(map(int,input().split()))
# f(arr,n)

# def f(arr,k,n):
#     c=0
#     if min(arr)<k:
#         c=1
#     for i in range(n-1):
#         for j in range(i+1,n+1):
#             if sum(arr[i:j])<k:
#                 c=max(c,j-i)
#             else:
#                 break
#     print(c)
# n=int(input())
# arr=list(map(int,input().split()))
# k=int(input())

# f(arr,k,n)
# def f(n,k,arr):
#     for i in range(n):
#         for j in range(i+1,n+1):
#             if sum(arr[i:j])==k:
#                 return [i+1,j]
# n = int(input())
# k=int(input())
# arr=list(map(int,input().split()))
# a =f(n,k,arr)
# print(a[0],a[1])


# n=int(input())
# b=[]
# arr=[]
# for i in range(n):
#     b.append(int(input()))
#     arr.append(i+1)
# a =0
# while 1:
#     a+=1
#     c = [None]*n 
#     for i in range(n):
#         c[i]=arr[b[i]-1]
#     if c==sorted(c):
#         break
#     arr=c
# print(a)

# def f(arr,n):
#     a=arr[0]
#     b=arr[0]
#     for i in range(1,n):
#         if arr[i]>a:
#             a=arr[i]
#         if arr[i]<b:
#             b=arr[i]
#     c=a
#     d=b
#     for i in range(n):
#         if c>arr[i] and arr[i]!=b:
#             c=arr[i]
#         if d<arr[i] and arr[i]!=a:
#             d=arr[i]
#     print("The highest element: ",a)
#     print("The smallest element: ",b)
#     print("The 2nd highest element: ",d)
#     print("The 2nd smallest element: ",c)
# arr=list(map(int,input().split()))
# n = len(arr)
# f(arr,n)

# def f(arr,n):
#     for i in range(n-1):
#         if arr[i]>arr[i+1]:
#             return False
#     return True
# arr=list(map(int,input().strip("{}").split(",")))
# n=len(arr)
# print(f(arr,n))

# def f(arr,n):
#     a=set()
#     i=0
#     for j in arr:
#         if j not in a:
#             a.add(j)
#             arr[i]=j
#             i+=1
#     return arr

# arr=list(map(int,input().split()))
# n=len(arr)
# print(f(arr,n))

# def a(arr1,arr2):
#     s=set(arr1)|set(arr2)
#     return sorted(s)
# arr1=list(map(int,input().split()))
# arr2=list(map(int,input().split()))
# print(a(arr1,arr2))

# def f(arr,n):
#     a=0
#     s=0
#     for i in range(n):
#         if arr[i]==1:
#             a+=1
#         else:
#             a=0
#         s=max(s,a)
#     return s
# arr=list(map(int,input().split()))
# n=len(arr)
# print(f(arr,n))

# def f(arr,n):
#     a=0
#     for i in range(n):
#         a=a^arr[i]
#     return a
# arr=list(map(int,input().split()))
# n=len(arr)
# print(f(arr,n))

# def f(arr,n,k):
#     m=0
#     a=0
#     b=0
#     s=arr[0]
#     while b<n:
#         while a<=b and s>k:
#             s-=arr[a]
#             a+=1
#         if s==k:
#             m=max(m,b-a+1)
#         b+=1
#         if b<n:
#             s+=arr[b]
#     print(m)
# arr=list(map(int,input().split()))
# n=len(arr)
# k=int(input())
# f(arr,n,k)

# def f(arr,n):
#     m=float('-inf')
#     s=0
#     for i in range(n):
#         s+=arr[i]
#         if s>m:
#             m=s
#         if s<0:
#             s=0
#     print(m)
# arr=list(map(int,input().split()))
# n=len(arr)
# f(arr,n)