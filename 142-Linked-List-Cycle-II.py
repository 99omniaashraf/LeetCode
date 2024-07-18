# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        \\\
        :type head: ListNode
        :rtype: ListNode
        \\\
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        
        # Step 1: Detect if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # No cycle found
            return None
        
        # Step 2: Find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

# Helper function to create a linked list with a cycle
def create_linked_list_with_cycle(arr, pos):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    cycle_node = None
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
        if i == pos:
            cycle_node = current
    if pos != -1:
        current.next = cycle_node
    return head
