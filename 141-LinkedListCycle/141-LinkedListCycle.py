# Last updated: 22:09:32 28/5/2026
1# Definition for singly-linked list.
2class ListNode:
3    def __init__(self, x):
4        self.val = x
5        self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        if head == None or head.next == None:
10            return False
11        
12        slow = head
13        fast = head
14
15        while fast and fast.next:
16            slow = slow.next
17            fast = fast.next.next 
18
19            if (slow == fast):
20                return True
21
22        return False