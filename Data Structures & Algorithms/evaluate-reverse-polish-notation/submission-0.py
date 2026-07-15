class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = list()
        operators: Dict[str] = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: int(x / y)}
        for token in tokens:
            if token in operators: 
                y: int = stack.pop()
                x: int = stack.pop()
                stack.append(operators[token](x,y))
            else:
                stack.append(int(token))

        return stack[0]