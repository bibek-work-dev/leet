class Solution:
    def isValid(self, s: str) -> bool:

        print(s)
        stack = Stacks()

        for i in s:
            is_empty = stack.is_empty()
            if is_empty:
                stack.push(i)
            else:   
                if not stack.is_empty() and stack.peek() == check_here[i]:
                    stack.pop()
                else:
                    stack.push(i)

        final_result_bool = stack.is_empty()
        if final_result_bool:
            return True
        else:
            return False

check_here = {"(": ")", "{": "}", "[": "]"}

class Stacks:
    # stacks = [] there are static variables. 
    # top = -1

    def __init__(self):
        self.stack = [] # this is correct. 
        self.top = -1

    def initialize_stack(self, input_string):
        self.stack = list(input_string)
        self.top = len(self.stack) - 1

    def push(self,char):
        # increase top and push to stack
        self.stack.append(char)
        self.top = self.top + 1

    def pop(self):
        if(self.top < 0):
            return
        self.stack.pop()
        self.top = self.top - 1
        # decrese the top value

    def peek(self):
        if(self.top < 0):
            return
        return self.stack[self.top]
        # give the element of top
    
    def is_empty(self):
        # check if top is -1
        if(self.top < 0):
            return True
        else:
            return False