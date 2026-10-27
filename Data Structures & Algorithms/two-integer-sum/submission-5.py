class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            x = target - nums[i]

            if x not in seen:
                seen[nums[i]] = i
            else:
                return [seen[x], i]
