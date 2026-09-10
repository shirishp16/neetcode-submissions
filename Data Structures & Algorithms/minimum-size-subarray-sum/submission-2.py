class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = 0
        total = 0
        l = 0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                if length == 0:
                    length = r - l + 1
                else:
                    length = min(r - l + 1, length)
                total -= nums[l]
                l += 1

        return length


        