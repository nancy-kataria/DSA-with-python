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
    
def binarySearch(num):
    # binary search works on a sorted array
    # O(log n) time complexity
    # O(1) space complexity
    lowestIndex = 0
    highestIndex = len(arr)-1

    while lowestIndex<=highestIndex:
        mid = (lowestIndex+highestIndex) // 2

        if arr[mid] == num:
            return mid
        elif num > arr[mid]:
            lowestIndex = mid+1
        else:
            highestIndex = mid-1

    return "Not Found"
    
def popElement(nums):
    # Elements have to be shifted when one element is removed from its position
    # O(n) time complexity
    # O(n) space complexity
    index = binarySearch(nums)
    arr.pop(index)
    
def reverseArray():
    # O(n) time complexity
    # O(n) space complexity - extra array space used
    # for reverse iteration, use -1 as the 3rd parameter
    # -1 is used as last index so that 0 is included
    # for index in range(len(arr)-1, -1, -1):
    #     arr2.append(arr[index])
    # return arr2

    # Swapping elements
    # O(n/2) = O(n) time complexity
    # O(1) space complexity
    arrayLength = len(arr)
    for index in range(0, arrayLength//2):
        temp = arr[index]
        arr[index] = arr[arrayLength-1]
        arr[arrayLength-1] = temp

    return arr

def rightRotation(nums,k):
    n = len(nums)
    if n <= 1:
        return nums

    # ex: 3%2 = 1 -> only one rotation
    if k > n:
        k = k % n

    return nums[n - k:] + nums[:n - k]

def inPlaceRotation(nums, k):
    n = len(nums)
    if n <= 1:
        return nums

    # ex: 3%2 = 1 -> only one rotation
    if k > n:
        k = k % n

    def reverse(start,end):
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1

    # reverse the whole array
    reverse(0, n-1)
    # reverse the first k-1 elements
    reverse(0,k-1)
    # reverse the rest
    reverse(k, n-1)

    return nums

def moveZeroesToEnd(nums):
    i = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1

    return nums