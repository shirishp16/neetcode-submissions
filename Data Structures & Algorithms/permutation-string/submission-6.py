class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        freq2 = {}
        l, r = 0, 0

        if len(s1) > len(s2):
            return False

        while r < len(s1):
            if s1[r] in freq:
                freq[s1[r]] += 1
            else:
                freq[s1[r]] = 1

            if s2[r] in freq2:
                freq2[s2[r]] += 1
            else:
                freq2[s2[r]] = 1

            r+=1

        if freq2 == freq:
                return True


        while r < len(s2):
            if s2[r] in freq2:
                freq2[s2[r]] += 1
            else:
                freq2[s2[r]] = 1
            
            freq2[s2[l]] -= 1

            if freq2[s2[l]] == 0:
                del freq2[s2[l]]

            if freq2 == freq:
                return True

            l += 1
            r += 1
            


        return False