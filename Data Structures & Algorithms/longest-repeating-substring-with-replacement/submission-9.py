class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        freq = {}
        l, r = 0, 0

        while r < len(s):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1

            if (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            else:
                longest = max(r-l+1, longest)
            r += 1

        return longest