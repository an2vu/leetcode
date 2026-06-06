# Last updated: 00:25:30 7/6/2026
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        min_len = float('inf')
4        f = 0
5        cur_sum = 0
6        for l in range(len(nums)):
7            cur_sum += nums[l]
8            while cur_sum >= target:
9                min_len = min(min_len, l-f+1)
10                cur_sum -= nums[f]
11                f +=1
12        
13        return min_len if min_len != float('inf') else 0
14
15
16