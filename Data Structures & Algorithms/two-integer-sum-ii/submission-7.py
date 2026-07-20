class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        li,ri = 0,len(numbers)-1
        while (li < ri):
            if numbers[li] + numbers[ri] == target:
                return [li+1,ri+1]
            elif numbers[li] + numbers[ri] > target:
                ri -=1
            elif numbers[li] + numbers[ri] < target:
                li +=1
            

            
