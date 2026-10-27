class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum=sum(nums[:k])
        sum_a=window_sum/k
        for i in range(k,len(nums)):
            window_sum=window_sum - nums[i-k] + nums[i]
            avg_sum=window_sum/k
            sum_a=max(sum_a,avg_sum)
        return sum_a
        