# Last updated: 22:42:16 31/5/2026
1
2class Solution:
3    def twoSum(self, nums: List[int], target: int) -> List[int]:
4        #init history
5        history = {}
6
7        for i, num in enumerate(nums):
8            key_pair = target - num
9            
10            #search history
11            if key_pair in history:
12                return [i, history[key_pair]]
13            
14            #update history
15            history[num] = i
16        return []
17            
18        