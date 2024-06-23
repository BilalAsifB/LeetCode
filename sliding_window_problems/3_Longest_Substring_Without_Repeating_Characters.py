def lengthOfLongestSubstring(s: str) -> int:
    """
    Given a string s, find the length of the longest 
    substring without repeating characters.
    """
    if s == '':
        return 0
    if len(s) == 1:
        return 1

    start = 0
    end = 0
    length = 1
    max_len = 1
    encountered = [s[start]]

    while end + 1 <= len(s) - 1:
        if s[end + 1] not in encountered:
            end += 1
            encountered.append(s[end])
            length += 1
            if length > max_len:
                max_len = length
        else:
            encountered.clear()
            start += 1
            end = start
            encountered.append(s[end])
            length = 1

    return max_len