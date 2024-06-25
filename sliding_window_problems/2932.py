def maximumStrongPairXor(nums: List[int]) -> int:
    """
    You are given a 0-indexed integer array nums. A pair of integers x and y 
    is called a strong pair if it satisfies the condition:
    |x - y| <= min(x, y)
    You need to select two integers from nums such that they form a strong pair 
    and their bitwise XOR is the maximum among all strong pairs in the array.
    Return the maximum XOR value out of all possible strong pairs in the array nums.
    """
    if len(nums) < 2 or nums[0] == set(nums):
        return 0

    max_xor = 0
    x = 0

    while x < len(nums) - 1:
        y = x + 1 
        while y < len(nums):
            if min(nums[x], nums[y]) >= abs(nums[x] - nums[y]):
                val = nums[x] ^ nums[y]
                if max_xor < val:
                    max_xor = val
            y += 1
        x += 1

    return max_xor