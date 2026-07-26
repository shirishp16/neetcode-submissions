class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { "(":")", "[":"]", "{":"}" }
        valid = False

        for c in s:
            if c in pairs:
                stack.append(pairs[c])
            elif len(stack) != 0:
                if c == stack.pop():
                    valid = True
                else:
                    return False
            else:
                return False

        if len(stack) != 0:
            return False

        return valid        