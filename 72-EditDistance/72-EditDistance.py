# Last updated: 5/30/2026, 10:48:21 AM
1from typing import List 
2
3
4class Solution:
5    def minDistance(self, word1: str, word2: str) -> int:
6        # this matrix keeps edit distance of two prefix 
7        matrix: List[List[int]] = [
8            [0 for _ in range(len(word2) + 1)]
9            for _ in range(len(word1) + 1)
10        ]
11
12        # init 
13        for i in range(len(word2) + 1): 
14            matrix[0][i] = i
15        for i in range(len(word1) + 1): 
16            matrix[i][0] = i
17
18        # dynamic programing
19        for i in range(1, len(word1) + 1): 
20            for j in range(1, len(word2) + 1): 
21                if word1[i-1] == word2[j-1]: 
22                    matrix[i][j] = matrix[i-1][j-1]
23                else: 
24                    matrix[i][j] = min(
25                        matrix[i-1][j] + 1,   # delete word2[i-1]
26                        matrix[i][j-1] + 1,    # delete word1[j-1]
27                        matrix[i-1][j-1] + 1    # replace word2[i-1] by word1[j-1]
28                    )
29
30        return matrix[-1][-1]
31    