from Empty import Empty


class LinkedStack:
    # Nested Node Class
    class Node:
        def __init__(self, element, next):
            self.__element = element
            self.__next = next

        def get_next(self):
            return self.__next

        def get_element(self):
            return self.__element

    def __init__(self):
        self.head = None
        self.size = 0
        self.data = []

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.data)

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        newest = self.Node(e, self.head)
        self.head = newest
        self.size += 1
        self.data.append(newest)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.head.__element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self.head.element
        self.head = self.head.next
        self.size -= 1
        return answer

