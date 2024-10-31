class Solution(object):
    def evalRPN(self, tokens):
        answer = 0
        stack = []
        if len(tokens) == 1:
            return tokens[0]
        for token in tokens:
            answer = None
            if token == '*':
                answer = stack.pop() * stack.pop()
            elif token == '+':
                answer = stack.pop() + stack.pop()
            elif token == '-':
                first = stack.pop()
                answer = stack.pop() - first
            elif token == '/':
                first = stack.pop()
                answer = int(float(stack.pop()) / first)
            else:
                stack.append(int(token))
            if answer != None:
                stack.append(answer)
        return answer

            