def linearSearch(num):
    # comparing one element with one we are searching
    # O(n) time complexity since we are traversing through the whole array - worst case
    # O(1) space complexity
    for index in range(0, len(arr)):
        if(arr[index] == num):
            return index

    return "Not Found"

arr = [2,6,11,3,7,23,4,62,43,9]

print(linearSearch(4))