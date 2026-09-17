class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        sum=0
        for i in digits:
            sum=sum*10+i
        sum=sum+1
            
        ret_val=[]
        while sum != 0:
            ret=sum%10
            
            ret_val.append(ret)
            sum=sum//10
        return ret_val[::-1]
        