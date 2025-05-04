# A linked list is a linear data structure that consists of a series of nodes connected by pointers (in C or C++)
# or references (in Java, Python and JavaScript). Each node contains data and a pointer/reference to the next node in the list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)

        # If list is empty, make node as the head
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head

        # keep traversing to the end of the list
        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = node

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        
        node.next = self.head
        self.head = node

    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head

        while counter != index:
            currentNode = currentNode.next
            counter+=1

        return currentNode
    
    def remove(self, index):
        if index == 0:
            unwantedNode = self.head
            self.head = unwantedNode.next
            return
        
        # traverse until the one node before the node to be removed
        leader = self.traverseToIndex(index-1)
        unwantedNode = leader.next
        leader.next = unwantedNode.next

    def reverse(self):
        prev = None
        current = self.head
        next = current.next

        while current:
            # set following variable to current's next node
            following = current.next
            # reverse the pointer of current node to prev node
            current.next = prev
            # move prev pointer to the current node
            prev = current
            # move current pointer to the next node
            current = following

        self.head = prev


    def printlist(self):
        currentNode = self.head
        arr = []
        while currentNode:
            arr.append(currentNode.value)
            currentNode = currentNode.next  # Move to the next node
        print(arr)


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.prepend(4)
linked_list.printlist()
linked_list.remove(2)
linked_list.printlist()
linked_list.reverse()
linked_list.printlist()