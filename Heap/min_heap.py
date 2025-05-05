import heapq

# Min Heap - Used in Priority Queues

# heapifying n elements = O(log n)
# popping one element =  O(log n) - it pops, as well as heapifies
# popping k elements = O(k log n) - k times

# similarly, heapifying k elements = O(log k)

def minHeap(data):
    heapq.heapify(data)
    print(data)

    # i - node index
    # node's left child - left(i) = 2*i+1
    # node's right child - right(i) = 2*i + 2

    # pops and heapifies
    print(heapq.heappop(data))

    print(data)

    # heap push adds and heapifies the data
    heapq.heappush(data, 2)
    heapq.heappush(data, 19)
    print(data)

minHeap([10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1])