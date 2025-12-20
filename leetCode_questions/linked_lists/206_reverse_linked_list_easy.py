# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we want to reverse the next values as we iterate through the linked list
        prev = None
        curr = head

        while curr:
            nextHead = curr.next  # save the next node
            curr.next = prev  # reverse the pointer
            prev = curr  # save the current node as previous node
            curr = nextHead  # set current node to next head
        return prev


