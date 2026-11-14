class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        freq = {0 : 0, 1 : 0}

        for n in students:
            if n == 0:
                freq[0] += 1
            elif n == 1:
                freq[1] += 1

        for i in range(len(sandwiches)):
            if freq[sandwiches[i]] == 0:
                break
            else:
                freq[sandwiches[i]] -= 1
        
        return (freq[0] + freq[1])


