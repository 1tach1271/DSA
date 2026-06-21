class Solution:
    def nameprint(self, name, count,num):
        if count==num:
            return
        print(name)

        self.nameprint(name,count+1,num)
if __name__ == "__main__":
    a=Solution()
    num = int(input())
    name = input()
    a.nameprint(name,0,num)