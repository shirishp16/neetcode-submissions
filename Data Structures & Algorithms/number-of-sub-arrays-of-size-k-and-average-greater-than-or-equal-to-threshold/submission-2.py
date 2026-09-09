class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        l = 0
        r = 0
        s = 0

        while r < k:
            s += arr[r]
            r += 1
        
        r -= 1

        for r in range(r, len(arr)):
            if r - l > k-1:
                s -= arr[l]
                l += 1
                s += arr[r]
            
            avg = s/k
            if avg >= threshold:
                count += 1
        
        return count
                