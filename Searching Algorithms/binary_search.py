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

arr = [2,5,6,11, 34, 36, 41]

print(binarySearch(5))