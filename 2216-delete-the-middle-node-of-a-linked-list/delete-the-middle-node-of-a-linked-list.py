class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Special case: if list has only one node
        if not head or not head.next:
            return None
        
        # Create a dummy node to handle cases where middle is the first node
        dummy = ListNode(0)
        dummy.next = head
        
        # Two pointers: slow and fast
        slow = dummy
        fast = head
        
        # Move pointers: fast moves 2 steps, slow moves 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Now slow is at the node before the middle node
        # Delete the middle node
        slow.next = slow.next.next
        
        return dummy.next