# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we want to iterate over both lists and have the node in list 1 point to the node of list 2 of the same index,
        # base case 0, in either list, return either list
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        # look at the first value of both lists, then set the head of new listnode to smaller value
        # look at the next value of both lists, then set the next of head to whichever head is smaller

        if list1.val <= list2.val:
            newListHead = list1
            list1 = list1.next
        else:
            newListHead = list2
            list2 = list2.next

        returnHead = newListHead

        while list1 is not None or list2 is not None:
            if list1 is None:
                newListHead.next = list2
                break
            elif list2 is None:
                newListHead.next = list1
                break
            elif list1.val <= list2.val:
                newListHead.next = list1
                list1 = list1.next
            else:
                newListHead.next = list2
                list2 = list2.next
            newListHead = newListHead.next
        return returnHead

        # we grab the next value of both lists, choose the lower value as next node




