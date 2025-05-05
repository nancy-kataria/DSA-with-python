stack = []

# O(1) - time complexity - all operations are performed on top of the stack
# O(1) - space complexity
def stackTop():
    return stack[len(stack)-1]

def stackIsEmpty():
    if stack:
        return False
    else:
        return True

stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()

print(stack)
print(stackTop())
stack.pop()
stack.pop()
print(stackIsEmpty())