class Solution:
    def isValid(self, s: str) -> bool:
        open_characters: Set[str] = {"(", "{", "["}
        matching_brackets: Dict[str, str] = {"(":")", "{": "}", "[": "]"}
        
        stack: List[str] = list()
        for bracket in s:
            if bracket in open_characters:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                open_bracket: str = stack.pop()
                if matching_brackets[open_bracket] != bracket:
                    return False
        
        return len(stack) == 0