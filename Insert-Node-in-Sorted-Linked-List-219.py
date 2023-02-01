# add in middle, add in head, add in tail
class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def insertNode(head, val):
    # create dummy node, dummy.next = head
    # 1. dummy.next always pointed to head
    # 2. easy to deal with when head = null
    # example as insert num is 0
    dummy = ListNode(float('-inf'))
    dummy.next = head
    curr_Node = dummy
    # 1. find the last node which <= val
    while curr_Node.next and curr_Node.next.val < val:
        curr_Node = curr_Node.next
    # 2. insert
    new_node = ListNode(val)
    new_node.next = curr_Node.next
    curr_Node.next = new_node

    return dummy.next


# Create a linked list: 1 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)

# Insert the value 2 into the linked list
head = insertNode(head, 2)

# Traverse the linked list to verify the result
curr = head
while curr:
    print(curr.val)
    curr = curr.next
