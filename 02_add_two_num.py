# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        i = 0
        val = l1.val + l2.val
        if val > 10:
            num = 1
            val = val - 10
        else:
            num = 0
        new_node = ListNode()
        new_node.val = val
        head = new_node
        current = head
        l1 = l1.next
        l2 = l2.next
        
        while(l1 or l2):
            if l1 is None:
                val = l2.val + num
                l2 = l2.next
            elif l2 is None:
                val = val = l1.val + num
                l1 = l1.next
            else:
                val = l1.val + l2.val + num
                l1 = l1.next
                l2 = l2.next
            
            if val >= 10:
                num = 1
                val = val - 10
            else:
                num = 0

            new_node = ListNode()
            new_node.val = val
            current.next = new_node
            current = current.next
        
        if num:
            new_node = ListNode()
            new_node.val = num
            current.next = new_node
            current = current.next

        while(head):
            print(head.val, end=" ")
            head=head.next

if __name__ == "__main__":
    l1 = ListNode(0)

    l2 = ListNode(0)

    s = Solution()
    result = s.addTwoNumbers(l1, l2)