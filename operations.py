import sys
class Operations: 

    def get_operands(self, stack):
        if len(stack) < 2: 
            print("Need 2 operands before operator! Now exiting...")
            sys.exit()
        return stack.pop(), stack.pop()

    def plus(self, stack):
        operand_one, operand_two =self.get_operands(stack)
        res = operand_two + operand_one
        stack.append(res)
        return res

    def minus(self, stack):
        operand_one, operand_two = self.get_operands(stack)
        res = operand_two - operand_one
        stack.append(res)
        return res

    def multiplication(self, stack):
        operand_one, operand_two = self.get_operands(stack)
        res = operand_two * float(operand_one)
        stack.append(res)
        return res

    def division(self, stack):
        operand_one, operand_two = self.get_operands(stack)
        if operand_one == 0: 
            print("Division by 0 not allowed :/. Now exiting...")
            sys.exit(0)
        res = operand_two / float(operand_one)
        stack.append(res)
        return res 
    