def removeNodeWithoutGivenHead(node):
    node.value = node.next.value
    node.next = node.next.next

    currentNode = node
    while currentNode:
        print(currentNode.value)
        currentNode = currentNode.next