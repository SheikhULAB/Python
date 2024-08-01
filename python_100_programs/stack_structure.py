class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == [] 
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Popped item: ", stack.pop())
print("Stack is empty: ", stack.is_empty())           