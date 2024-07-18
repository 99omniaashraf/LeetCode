# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        \\\
        :type head1, head1: ListNode
        :rtype: ListNode
        \\\
        # Get the lengths of both linked lists
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        lenA = get_length(headA)
        lenB = get_length(headB)
        
        # Align the starting points
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        
        # Traverse both lists together to find the intersection point
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None

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
