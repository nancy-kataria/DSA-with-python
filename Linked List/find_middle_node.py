def findMiddleNode(head):
    slowPointer, fastPointer = head, head

    while fastPointer is not None and fastPointer.next is not None:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next

    return slowPointer