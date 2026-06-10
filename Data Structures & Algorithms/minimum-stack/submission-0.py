class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.top_ele = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.top_ele == -1:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val,self.min_stack[self.top_ele]))
        self.top_ele += 1

    def pop(self) -> None:
        self.stack.pop(-1)
        self.min_stack.pop(-1)
        self.top_ele -= 1

    def top(self) -> int:
        return self.stack[self.top_ele]

    def getMin(self) -> int:
        return self.min_stack[self.top_ele]
