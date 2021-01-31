class Stack:
    def __init__(self):
        self.__list = []

    def push(self, val):
        self.__list.append(val)

    def pop(self):
        return self.__list.pop()

    def __iter__(self):
        return iter(self.__list)


stack = Stack()
stack.push(1)
stack.push(2)

for s in stack:
    print(s)

