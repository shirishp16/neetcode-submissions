class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        lowest = r

        while l <= r:
            mid = (l + r) // 2

            hrs = 0
            for n in piles:
                hrs += n // mid
                if n % mid != 0:
                    hrs += 1
            
            if hrs > h:
                l = mid +1
            elif hrs <= h:
                lowest = min(lowest, mid)
                r = mid -1
        
        return lowest
