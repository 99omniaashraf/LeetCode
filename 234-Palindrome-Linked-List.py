# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        \\\
        :type head: ListNode
        :rtype: bool
        \\\
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Step 3: Compare the first half and the reversed second half
        first_half = head
        second_half = prev
        
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        # Optionally, restore the list to its original state here (not required for palindrome check)
        
        return True

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the list (for testing purposes)
def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)
