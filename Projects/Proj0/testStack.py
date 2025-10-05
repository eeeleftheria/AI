import parentheses

print("Testing stack with integers")
myStack = parentheses.Stack() # creation of object Stack

for i in range(10):
    myStack.push(i)

myStack.printStack()

myStack.pop()
myStack.printStack()

#myStack.pop()
#myStack.printStack()


myStack.push(32)
myStack.printStack()

print("Testing stack with both integers and strings")

isEmpty = myStack.empty()
if isEmpty == False:
    size = myStack.size
    for i in range(size):
        myStack.pop()


myStack.printStack()

myStack.push('s')
myStack.push(6)
myStack.push(9)
myStack.push("str")
myStack.push('m')

myStack.printStack()

myStack.pop()
myStack.printStack()




