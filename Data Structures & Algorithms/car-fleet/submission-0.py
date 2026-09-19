class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i, pos in enumerate(position):
            t = (target - pos) / speed[i]
            cars.append([pos, t])

        cars.sort(reverse=True)

        stack = []

        for pos, t in cars:
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)