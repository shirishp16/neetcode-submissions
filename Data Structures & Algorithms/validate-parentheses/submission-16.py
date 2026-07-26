class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { "(":")", "[":"]", "{":"}" }

        for c in s:
            if c in pairs:
                stack.append(pairs[c])
            elif len(stack) != 0:
                if c != stack.pop():
                    return False
            else:
                return False

        return len(stack) == 0     