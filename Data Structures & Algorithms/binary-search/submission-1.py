class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = 0
        mid = (r - l) // 2

        while l <= r:
            if target > nums[mid]:
                l = mid + 1
                mid = (r + l) // 2
            elif target < nums[mid]:
                r = mid - 1
                mid = (r + l) // 2
            if target == nums[mid]:
                return mid


        return -1
        