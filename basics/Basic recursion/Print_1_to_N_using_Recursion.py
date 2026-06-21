class Solution:
    def pattern(self,count,num):
        if count==num+1:
            return
        print(count,end=" ")
        self.pattern(count+1,num)
if __name__=="__main__":
    a=Solution()
    num = int(input("Entern the number"))
    a.pattern(1,num)