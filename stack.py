#!/usr/bin/env python3

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# test
s=Stack()

print(s.is_empty())
s.push('a')
s.push('b')
print(s.peek())
print(s.size())
print(s.is_empty())
s.push('c')
print(s.pop())
print(s.pop())
print(s.size())

