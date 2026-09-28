class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        lowest = min(nums[r], nums[l])

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] <= nums[l]:
                r = mid - 1
            lowest = min(lowest, nums[mid], nums[l], nums[r])
        
        return lowest
