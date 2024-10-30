class MinStack(object):
    class Node(object):
        def __init__(self, val, min):
            self.val = val
            self.min = min(val, min)

    def __init__(self):
        self.stack = []

    def push(self, val):
        min_val = None
        if len(self.stack == 0):
            min_val = 1e12
        else:
            min_val = self.topNode().min()
        self.stack.append(MinStack.Node(val, min_val))
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        self.stack.pop()
        """
        :rtype: None
        """
        

    def top(self):
        return self.stack[-1].val()
        """
        :rtype: int
        """
    def topNode(self):
        return self.stack[-1]    

    def getMin(self):
        return self.topNode().min()
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()