# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        ans=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        ans=count-n
        if ans==0:
            return head.next
        temp=head
        for i in range(ans-1):
            temp=temp.next
        temp.next=temp.next.next
        return head
    

        
        