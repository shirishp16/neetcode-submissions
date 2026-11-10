class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            curr = operations[i]
            if curr == '+':
                stack.append(stack[-1] + stack[-2])
            elif curr == 'C':
                stack.pop()
            elif curr == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(curr))

        res = 0
        for n in stack:
            res += n

        return res
