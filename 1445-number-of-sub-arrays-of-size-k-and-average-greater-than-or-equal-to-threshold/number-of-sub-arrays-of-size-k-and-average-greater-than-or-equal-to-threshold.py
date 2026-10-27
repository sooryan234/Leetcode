class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        max_avg = (window_sum)/k
        count=0
        if max_avg >= threshold:
            count=count+1

        for i in range(k,len(arr)):
            window_sum = window_sum - arr[i - k] + arr[i]
            max_avg = window_sum / k
            if max_avg >= threshold:
                count=count+1
        return count