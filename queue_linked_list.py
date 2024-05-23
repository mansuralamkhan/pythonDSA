
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        else:
            removed_item = self.front.data
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            return removed_item
        
    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

        



q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

print("Queue elements:")
q.display()

# Dequeue elements
print("Dequeued item:", q.dequeue())
print("Dequeued item:", q.dequeue())

# Display the updated queue
print("Queue elements after dequeuing:")
q.display()

