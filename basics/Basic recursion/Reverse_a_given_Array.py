def pattern(arr):
    arr[:]=arr[::-1]
if __name__=="__main__":
    arr = [1,2,3,4,5]
    pattern(arr)
    print(" ".join(map(str,arr)))