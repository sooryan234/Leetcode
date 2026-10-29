class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # f=False
        # for i in range(len(nums)):
        #     for j in range (i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             if abs(i-j) <= k:
        #                 f= True
        # return f
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])

        return False
                
