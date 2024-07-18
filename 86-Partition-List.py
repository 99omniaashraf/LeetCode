# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        \\\
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        \\\
        # Create two dummy nodes to act as the heads of the less and greater lists
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Create pointers to the current nodes in the less and greater lists
        less = less_head
        greater = greater_head
        
        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        # End the greater list
        greater.next = None
        
        # Connect the less list with the greater list
        less.next = greater_head.next
        
        # Return the head of the less list
        return less_head.next

# Helper function to print the list (for testing purposes)
def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)
