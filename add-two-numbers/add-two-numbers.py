# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_value = 0
        l2_value = 0
        
        num = 1
        while l1 :
            l1_value += l1.val*num
            l1 = l1.next
            num *= 10
            
        num = 1
        while l2 :
            l2_value += l2.val*num
            l2 = l2.next
            num *= 10
            
        total = str(l1_value + l2_value)
        
        answer = None
        for x in reversed(total):
            if not answer :
                answer = ListNode(val = int(x))
                head = answer
            else :
                head.next=ListNode(val = int(x))
                head = head.next
        
        return answer