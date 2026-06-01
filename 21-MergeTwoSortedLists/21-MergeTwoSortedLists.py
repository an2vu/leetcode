# Last updated: 23:32:11 1/6/2026
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8
9        #init marge list
10        mergeList = ListNode()
11        tailList = mergeList
12
13        #point each node in list1 list2, compare and merge to mergeList
14
15        while list1 and list2:
16            if list1.val < list2.val:
17                tailList.next = list1
18                list1 = list1.next
19            else:
20                tailList.next = list2
21                list2 = list2.next
22            tailList = tailList.next
23        # add last node 
24        tailList.next = list1 if list1 else list2
25        return mergeList.next
26
27