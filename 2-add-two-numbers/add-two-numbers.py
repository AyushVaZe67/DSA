# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head for the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both lists while there are nodes or carry exists
        while l1 or l2 or carry:
            # Get values from current nodes (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node for the result
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_head.next