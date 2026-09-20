class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i, p in enumerate(position):
            t = (target - p) / speed[i]
            cars.append([p, t])

        cars.sort(reverse=True)

        stack = []

        for pos, time in cars:
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
                
            
            