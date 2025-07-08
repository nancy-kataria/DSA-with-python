# Auxiliary space refers to the extra space or the temporary space that an algorithm uses.
# Space complexity is the total space taken up by the algorithm with respect to the input size.

# Array is a linear data structure where all elements are arranged sequentially. It is a collection of elements of same data type
arr = []

# adding the element at the end
def arrayInsertion(num):
    # Time Complexity: O(1) (Amortized)
    # Space Complexity: O(1)
    # involves updating the array’s size and placing the new element in the next available position
    # all the nodes that precede the given node are not affected by this operation
    arr.append(num)
    
def elementAtIndex(index):
    # Time Complexity; O(1)
    # Space Complexity: O(1)
    # it directly computes the memory location of the element
    return arr[index]

def insertAtPosition(num, index):
    #  cannot be done this way because size of array is fixed here
    # for index in range(0, len(arr)-1):
    #     arr[index+1] = arr[index]
    #     if(index == 0):
    #         arr[index] = num

    # Since elements are shifted after insertion
    # O(n) time complexity
    arr.insert(index, num)