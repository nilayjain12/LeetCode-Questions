# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        Approach 1: Two pointers
        '''
        # # initialize previous and current pointers
        # prev = None
        # current = head

        # # loop to iterate until current becomes null
        # while current:
        #     temp = current.next
        #     current.next = prev
        #     prev = current
        #     current = temp
        
        # return prev

        '''
        Approach 2: One Pointer
        '''
        current = head
        head = None

        # iterate current through until None
        while current:
            next_node = current.next
            current.next = head
            head = current
            current = next_node
        
        return head