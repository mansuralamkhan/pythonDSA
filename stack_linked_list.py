class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        popped_data = self.top.data
        self.toop = self.top.next
        return popped_data
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data
stack = Stack()
elements = input("Enter the elements:").split()
for element in elements:
    for element in elements:
        stack.push(element)

print("Top element", stack.peek())
print("Popped element:", stack.pop())
print("Top element after pop", stack.peek())

    