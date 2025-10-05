import sys
# argument example: ()[{}]()

class Stack:

    # initialize empty stack
    # stack consits of a list of elements and a variable size
    def __init__(self):
        self.size = 0
        self.elements = [] # creation of empty list
        
    def push(self, value):

        #print(f"Pushing element {value}")
        
        self.elements.append(value) # add element at the top of the stack
        self.size += 1

        return None

    def pop(self):
        
        #print("Popping element from stack")
        
        if self.size == 0:
            print("Stack is empty")
            return None
                
        self.elements.pop() # remove most recently added element(top of stack)
        self.size -= 1

        return None
    
    # checks if stack is empty
    def empty(self):

        if self.size == 0:
            return True
        
        return False;
    
    def printStack(self):
        
        if self.size == 0:
            print("Empty stack")
            return None

        for i in range(self.size):
            print(self.elements[i])
    



if __name__ == '__main__':

    newStack = Stack()  # creation of stack that will store each parenthesis

    # we need a sequence of parentheses as an argument
    if len(sys.argv) != 2:
        print(f"Use: python {sys.argv[0]} sequence")
        sys.exit(1)

    inputStr = sys.argv[1] # the string is the 2nd argument: 1st is the name of the program   

    # add continuous open parenthesis to the stack until a closed one is reached ({((...)
    for i in range(len(inputStr)):

        ch = inputStr[i] # current character
        
        # when closed parenthesis is met
        # stop adding elements to the stack
        if ch == ')' or ch == ']' or ch == '}':

            # the last element of the stack must be
            # equal to the closing parenthesis met
            # else it is not balanced.
            # after checking if they are equal, last must be popped out of the stack

            # if the stack is empty and we have read a closing parenthesis,
            # then it is not balanced, since there cannot be only a closing one
            # without a corresponding open one
            if newStack.empty() == True:
                print("Not balanced 1")
                sys.exit(1)


            if ch == ')':
                if newStack.elements[newStack.size - 1] != '(':
                    print("Not balanced 2")
                    sys.exit(1)
            
            
            if ch == '}':
                if newStack.elements[newStack.size - 1] != '{':
                    print("Not balanced 3")
                    sys.exit(1)

            
            if ch == ']':
                if newStack.elements[newStack.size - 1] != '[':
                    print("Not balanced 4")
                    sys.exit(1)
            

            # till now is balanced:
            # last element is checked: pop it and go to next one
            newStack.pop()  
    
            # continue to next iteration, we do not want to add the closing parentheses to the stack
            continue 
            

        # push open parentheses
        newStack.push(inputStr[i])
 

    # after iterating through the whole string, 
    # if it was indeed balanced, no parentheses should
    # be left in the stack
    if newStack.empty() == False:
        print("Not balanced")
        sys.exit(0)

    print(" Balanced")
    sys.exit(0)