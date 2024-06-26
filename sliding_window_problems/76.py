from collections import Counter

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        """
        Given two strings s and t of lengths m and n respectively, return the minimum 
        window substring of s such that every character in t (including duplicates) is 
        included in the window. If there is no such substring, return the empty string "".
        """
        if len(s) < len(t):
            return ""
        
        t_freq = Counter(t)
        match_count = 0
        start = 0
        res_start = 0
        min_len = len(s) + 1
        
        for index, char in enumerate(s):
            if char in t_freq:
                t_freq[char] -= 1
                match_count += t_freq[char] == 0

            while match_count == len(t_freq):
                if min_len > index - start + 1:
                    min_len = index - start + 1
                    res_start = start
                
                char_r = s[start]
                start += 1

                if char_r in t_freq:
                    match_count -= t_freq[char_r] == 0
                    t_freq[char_r] += 1

        return s[res_start:res_start + min_len] if min_len <= len(s) else ""
    
if __name__ == "__main__":
    s = Solution()
    res = s.minWindow("ADOBECODEBANC", "ABC")
    print(res)