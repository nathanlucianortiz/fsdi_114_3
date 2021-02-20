class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# test
q=Queue()

print(q.is_empty())
q.enqueue('a')
q.enqueue('b')
print(q.size())
print(q.is_empty())
q.enqueue('c')
print(q.dequeue())
print(q.dequeue())
print(q.size())
