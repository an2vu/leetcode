# Last updated: 00:12:34 4/6/2026
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        ListNodeWell = head
9        while ListNodeWell and  ListNodeWell.next :
10            if ListNodeWell.val == ListNodeWell.next.val:
11                ListNodeWell.next = ListNodeWell.next.next
12            else:
13                ListNodeWell = ListNodeWell.next
14        return head
15
16