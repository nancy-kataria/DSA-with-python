def removeDuplicates(head):
    if head is None:
        return []

    currentNode = head
    nextNode = head.next

    while nextNode:
        if currentNode.value == nextNode.value:
            currentNode.next = nextNode.next
            nextNode=nextNode.next
        else:
            currentNode = currentNode.next
            nextNode = nextNode.next

    node = head
    arr = []
    while node:
        arr.append(node.value)
        node = node.next  # Move to the next node

    return arr