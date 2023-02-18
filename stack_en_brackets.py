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

s = Stack()

print(s.is_empty())
s.push('3.14')
s.push('python')
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(2.71828)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.size())

def check_balance (x,y):
    if x == '(' and y == ')' or x == '[' and y == ']' or x == '{' and y == '}':
        return True
    else:
        return False

def Balanced_Brackets(string):

    brbrbr = Stack()
    for el in string:
        if brbrbr.is_empty():
            brbrbr.push(el)
        else:
            if check_balance(brbrbr.peek(), el) == True:
                brbrbr.pop()
            else:
                brbrbr.push(el)

    if brbrbr.is_empty():
        print("Сбалансировано")
    else:
        print("Несбалансировано")

string1 = "(((([{}]))))"
Balanced_Brackets(string1)
string2 = "[([])((([[[]]])))]{()}"
Balanced_Brackets(string2)
string3 = "{{[()]}}"
Balanced_Brackets(string3)
string4 = "}{}"
Balanced_Brackets(string4)
string5 = "{{[[(])]}}"
Balanced_Brackets(string5)
string6 = "[[{())}]"
Balanced_Brackets(string6)