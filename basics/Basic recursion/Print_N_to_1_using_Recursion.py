class Solution:
    def pattern(self, num):
        if num<1:
            return
        print(num,end=" ")
        self.pattern(num-1)
if __name__=="__main__":
    a = Solution()
    num = int(input("Enter the num "))
    a.pattern(num)