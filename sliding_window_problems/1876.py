from collections import deque

def countGoodSubstrings(s: str) -> int:
    """
    A string is good if there are no repeated characters. Given a string s
    return the number of good substrings of length three in s. 
    Note that if there are multiple occurrences of the same substring, 
    every occurrence should be counted.
    A substring is a contiguous sequence of characters in a string.
    """
    if len(s) < 3 or not s:
        return 0

    count = 0
    check = deque()

    for i in range(3):
        check.append(s[i])

    if len(set(check)) == 3:
        count += 1

    end = 3

    while end <= len(s) - 1:
        check.popleft()
        check.append(s[end])
        end += 1

        if len(set(check)) == 3:
            count += 1            

    return count