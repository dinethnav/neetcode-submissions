# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        if not head or head.next is None:
            return head
        while head.next is not None:
            if len(stack) == 0:
                stack.append(ListNode(head.val))
            else:
                next_node = stack.pop()
                stack.append(ListNode(head.val,next_node))
            head = head.next
        
        return ListNode(head.val,stack[-1])
        