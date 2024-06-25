from collections import deque

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    """
    You are given an array of integers nums, there is a sliding window of size k 
    which is moving from the very left of the array to the very right.
    You can only see the k numbers in the window. Each time the sliding window 
    moves right by one position. Return the max sliding window.
    """
    if len(nums) == 0 or k == 0:
        return []

    res = []
    arr = deque()

    for i in range(len(nums)):
        if arr and arr[0] < i - k + 1:
            arr.popleft()
        
        while arr and nums[arr[-1]] < nums[i]:
            arr.pop()
        
        arr.append(i)
        
        if i >= k - 1:
            res.append(nums[arr[0]])
    
    return res
