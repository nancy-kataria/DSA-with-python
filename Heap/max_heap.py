import heapq

def maxHeap(data):
    # to implement maxheap, we make all numbers negative
    # so that bigger number, say -1000 is at top
    maxheap = [-num for num in data]
    heapq.heapify(maxheap)

    print(maxheap)
    # O(log n) time complexity for heappop
    print(-heapq.heappop(maxheap))

maxHeap([10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1])