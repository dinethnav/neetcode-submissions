# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        merged_ll = head

        while list1 and list2:
            if list1.val < list2.val:
                merged_ll.next = ListNode(list1.val)
                merged_ll = merged_ll.next
                list1 = list1.next
            else:
                merged_ll.next = ListNode(list2.val)
                merged_ll = merged_ll.next
                list2 = list2.next

        if list1:
            merged_ll.next = list1
        else:
            merged_ll.next = list2

        return head.next
                
        