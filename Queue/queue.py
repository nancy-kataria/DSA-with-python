
# deque is a double-ended queues
# supports efficient insertion and deletion operations from both ends (front and rear) of the queue
from collections import deque
# Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container

# if we use a list to implement queue, popping an element will result in O(n) time complexity due to shifting of elements
# whereas using popleft in deque provides O(1) time complexity

# Why use deque instead of queue?
# queue.Queue and collections.deque serve different purposes. queue.Queue is intended for allowing different
# threads to communicate using queued messages/data, whereas collections.deque is simply intended as a data structure.
# That's why queue.Queue has methods like put_nowait(), get_nowait(), and join(), whereas collections.deque doesn't.
# queue.Queue isn't intended to be used as a collection, which is why it lacks the likes of the in operator.

# It boils down to this: if you have multiple threads and you want them to be able to communicate without the need for locks,
# you're looking for queue.Queue; if you just want a queue or a double-ended queue as a datastructure, use collections.deque.

queueList = deque()

# If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
def enqueue(nums):
    queueList.append(nums)

# The items are popped in the same order in which they are pushed.
# If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
def dequeue():
    queueList.popleft()

enqueue(1)
enqueue(2)
enqueue(3)
dequeue()

print(queueList)
