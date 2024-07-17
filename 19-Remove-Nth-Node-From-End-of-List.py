# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        \\\
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        \\\
        # Create a dummy node pointing to the head of the list
        dummy = ListNode(0, head)

        # Initialize two pointers, both starting from the dummy node
        first = dummy
        second = dummy

        # Move the first pointer n+1 steps forward to ensure a gap of n between the pointers
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until the first pointer reaches the end of the list
        while first is not None:
            first = first.next
            second = second.next

        # Now, second pointer is pointing to the node just before the node to be removed
        # Change the next pointer of the second pointer to skip the desired node
        second.next = second.next.next

        # Return the head of the modified list after removing the node
        return dummy.next