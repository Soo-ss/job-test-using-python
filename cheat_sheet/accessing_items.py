class Stack:
    def __init__(self):
        self.__list = []

    def push(self, val):
        self.__list.append(val)

    def pop(self):
        return self.__list.pop()

    def __repr__(self):
        return "{}".format(self.__list)

    def __len__(self):
        return len(self.__list)

    def __getitem__(self, idx):
        return self.__list[idx]

    def __setitem__(self, idx, val):
        self.__list[idx] = val


stack = Stack()
stack.push(1)
stack.push(2)
print("stack:", stack)

stack[0] = 3
print("stack: ", stack)
print("num items: ", len(stack))
