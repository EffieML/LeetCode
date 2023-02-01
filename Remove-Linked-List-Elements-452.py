# Remove all elements from a linked list of integers that have value val.
# val can be at head, middle and tail
class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def removeElements(head, val):
    # create dummy node, dummy.next = head
    # 1. dummy.next always point to head
    # 2. easy to deal with when head = null
    dummy = ListNode(0)
    dummy.next = head
    currNode = dummy

    while currNode.next:
        # if currNode.next is val, than exclude
        if currNode.next.val == val:
            currNode.next = currNode.next.next
        # if currNode.next not val, than move to next
        else:
            currNode = currNode.next
    return dummy.next

    # Create a linked list: 1 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
