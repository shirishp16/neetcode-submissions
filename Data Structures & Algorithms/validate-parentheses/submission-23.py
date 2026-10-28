class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        comp = {"]" : "[", "}" : "{", ")" : "(" } 

        for c in s:
            if c not in comp:
                stack.append(c)
            else:
                if not stack or stack.pop() != comp[c]:
                    return False
            
        return not stack