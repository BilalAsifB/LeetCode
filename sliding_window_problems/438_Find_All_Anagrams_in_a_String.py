def findAnagrams(self, s: str, p: str) -> List[int]:
    """
    Given two strings s and p, return an array of all the start indices of 
    p's anagrams in s. You may return the answer in any order.
    """
    if len(s) < len(p):
        return []

    indexes = []
    s_freq = [0] * 26
    p_freq = [0] * 26

    for i in range(len(p)):
        s_freq[ord(s[i]) - ord('a')] += 1
        p_freq[ord(p[i]) - ord('a')] += 1

    if s_freq == p_freq:
        indexes.append(0)

    start = 0
    end = len(p)

    while end < len(s):
        s_freq[ord(s[start]) - ord('a')] -= 1
        s_freq[ord(s[end]) - ord('a')] += 1
        
        if s_freq == p_freq:
            indexes.append(start + 1)
        
        start += 1
        end += 1

    return indexes