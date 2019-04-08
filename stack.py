class Stack:
    def __init__(self):
        self.items= []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def get_stack(self):
        print(f"The list is{self.items}")

    def peek(self):
        return self.items[-1]



s = Stack()
s.push('A')
s.push('B')
s.push('C')
s.get_stack()
s.pop()
s.get_stack()
print(s.peek())


########################################################################


class Stack:
    def __init__(self):
        self.items= []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def get_stack(self):
        return self.items
    def is_empty(self):
        return self.items == []
    def not_empty(self):
        return self.items != []

    def peek(self):
        if self.not_empty():
            print(self.items[-1])
        else:
            print('The list is empty!')

    def get_size(self):
        return len(self.items)




s = Stack()
s.push('A')
s.push('B')
s.push('C')
print(s.get_stack())
print(s.get_size())
s.pop()
print(s.get_stack())
print(s.is_empty())
print(s.not_empty())
s.pop()
s.pop()
s.peek()

##########################################################
