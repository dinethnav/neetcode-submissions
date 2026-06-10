# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []

        while head:
            stack.append(head.val)
            head = head.next

        new_head = None

        for i in range(1,n):
            if new_head is None:
                new_head = ListNode(stack.pop())
            else:
                new_head = ListNode(stack.pop(),new_head)

        if len(stack) < 2:
            return new_head
        
        stack.pop()
        while len(stack) > 0:
            new_head = ListNode(stack.pop(),new_head)

        return new_head


        
        