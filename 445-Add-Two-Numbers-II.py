# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        \\\
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        \\\
        stack1 = []
        stack2 = []
        
        # Push all nodes' values of l1 onto stack1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        # Push all nodes' values of l2 onto stack2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None
        
        # Process the stacks
        while stack1 or stack2 or carry:
            sum = carry
            if stack1:
                sum += stack1.pop()
            if stack2:
                sum += stack2.pop()
            
            carry = sum // 10
            node = ListNode(sum % 10)
            node.next = head
            head = node
        
        return head

# Helper function to print the list (for testing purposes)
def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)
