class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        def isNumber(num):
            return num.rstrip().lstrip("-").isdigit()

        def calc(op1,op2,opr):
            match opr:
                case '+':
                    return op1+op2
                case '-':
                    return op1-op2
                case '*':
                    return op1*op2
                case '/':
                    return int(op1/op2)
        op_stack = []
        while len(tokens)>0:
            while isNumber(tokens[0]):
                op_stack.append(int(tokens.pop(0)))
            else:
                opr = tokens.pop(0)
                op2 = op_stack.pop(-1)
                op1 = op_stack.pop(-1)
                res = calc(op1,op2,opr)
                op_stack.append(res)
        return op_stack[0]


            
        
         
            

            