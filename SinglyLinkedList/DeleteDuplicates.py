# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if (head == None):
            return head

        current = head
        nextVal= None

        while(current.next != None):
            if current.val == current.next.val:
                nextVal = current.next.next
                #delete current.val
                current.next = nextVal
            else:
                current = current.next 
                
        return head


        