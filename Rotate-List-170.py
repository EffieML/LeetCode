# Given a list, rotate the list to the right by k places, where k is non-negative
# input 1-2-3-4-5, k = 7
# output 4-5-1-2-3
class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def getLength(self, head):
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        return length

    def rotateRight(self, head, k):
        if head is None:
            return None

        # create dummy node, dummy.next = head
        # 1. head will move
        # 2. dummy.next always point to head node
        dummy = ListNode(0)
        dummy.next = head

        length = self.getLength(head)
        # use linked list length mod to get rid of un-nessessary loop
        k = k % length

        ahead = dummy
        # move the ahead node step k
        for i in range(k):
            ahead = ahead.next
        # then move both ahead and behind node, until the ahead node reach to the end
        behind = dummy
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        # break the linked list and rearrange
        ahead.next = dummy.next
        dummy.next = behind.next
        behind.next = None

        return dummy.next


# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# Insert the value 2 into the linked list
obj = ListNode(None)
output = obj.rotateRight(head, 7)
# print(output.val)

# Traverse the linked list to verify the result
curr = output
while curr:
    print(curr.val)
    curr = curr.next
