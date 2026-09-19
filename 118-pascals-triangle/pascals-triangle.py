class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        first=[]
        for i in range(numRows):
            second = [1] * (i+1)
            for j in range(1,i):
                second[j]=first[i-1][j-1]+first[i-1][j]
            first.append(second)
        return first

        





        