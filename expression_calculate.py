import sys
import re
import operator

operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

class Stack:

    def __init__(self):
        self.stack = []

    def push_(self,e):
        self.stack.append(e)
        return self.stack

    def pop_(self):
        try:
            removed = self.stack[len(self.stack) -1]
            del self.stack[len(self.stack) -1]
            return removed
        except:
            print("cannot pop from an empty array, error: ", sys.exc_info()[0])

    def isEmpty_(self):
        return len(self.stack) == 0

def arithmetic_operations_stack(expression, operators):

    stack = Stack()
    result_str = str(expression[0])
    
    for i in range(len(expression)):
        print(expression[i])
        if not (expression[i] in operators.keys()): ## isnt an operator
            stack.push_(expression[i])
        else:
            e2 = stack.pop_()
            e1 = stack.pop_()
            e3 = operators[expression[i]](e1,e2)
            result_str = "(" + result_str + expression[i] + str(e2) + ")"
            stack.push_(e3)
    return result_str + "= " + str(stack.pop_())

print(arithmetic_operations_stack([6,4,"-",3,"*",10,"+",11,13,"-","*"], operators))


