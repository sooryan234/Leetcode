class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        window_sum = sum(ch in vowels for ch in s[:k])
        max_count = window_sum

        for i in range(k, len(s)):
            # window_sum -=int( s[i-k] in vowels)
            # window_sum += int(s[i] in vowels)
            # max_count = max(max_count, window_sum)
            if s[i-k] in vowels:
                window_sum=window_sum-1
            if s[i] in vowels:
                 window_sum=window_sum+1
            max_count=max(max_count, window_sum)

        return max_count

           
        