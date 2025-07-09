from linked_list import Node

def mergeSortedLists(list1, list2):
    outputListNode = Node(None)
    mergedNode = outputListNode

    while list1 and list2:
        if list1.value <= list2.value:
            mergedNode.next = list1
            list1 = list1.next
        else:
            mergedNode.next = list2
            list2 = list2.next
        mergedNode= mergedNode.next


    if list1:
        mergedNode.next = list1
    elif list2:
        mergedNode.next = list2

    currentnode = outputListNode.next
    arr = []
    while currentnode:
        arr.append(currentnode.value)
        currentnode = currentnode.next  # Move to the next node

    return arr