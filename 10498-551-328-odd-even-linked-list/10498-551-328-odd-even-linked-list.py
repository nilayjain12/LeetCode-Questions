# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        evenStart = even

        while odd != None and odd.next != None and even != None and even.next != None:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenStart

        return head