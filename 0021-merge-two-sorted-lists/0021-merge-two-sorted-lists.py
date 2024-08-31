# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        finalHead, resList = ListNode()
        
        cur1, cur2 = list1, list2

        while cur1 and cur2:
            if cur1.value >= cur2.value:
                resList.next = cur2
                cur2 = cur2.next
                resList = resList.next
            else:
                resList.next = cur1
                cur1 = cur1.next
                resList = resList.next

        if cur1:
            resList.next = cur1
        if cur2:
            resList.next = cur2
        return finalHead

            