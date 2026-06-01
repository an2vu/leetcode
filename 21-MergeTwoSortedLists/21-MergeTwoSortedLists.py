# Last updated: 23:34:11 1/6/2026
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6"""
7pattern: two pointer
8"""
9
10class Solution:
11    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
12
13        #init marge list
14        mergeList = ListNode()
15        tailList = mergeList
16
17        #point each node in list1 list2, compare and merge to mergeList
18
19        while list1 and list2:
20            if list1.val < list2.val:
21                tailList.next = list1
22                list1 = list1.next
23            else:
24                tailList.next = list2
25                list2 = list2.next
26            tailList = tailList.next
27        # add last node 
28        tailList.next = list1 if list1 else list2
29        return mergeList.next
30
31