# Find the middle node of a linked list
class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def middleNode(head):
    if head is None:
        return None

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# Create a linked list: 1 -> 3 -> 4 -> 6
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(6)

# Insert the value 2 into the linked list
output = middleNode(head)
print(output.val)

# Traverse the linked list to verify the result
# curr = head
# while curr:
#     print(curr.val)
#     curr = curr.next
