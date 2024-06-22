class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        left_max = height[start]
        right_max = height[end]
        vol = 0

        while start < end:
            if left_max < right_max:
                vol += left_max - height[start]
                start += 1
                left_max = max(left_max, height[start])
            else:
                vol += right_max - height[end]
                end -= 1
                right_max = max(right_max, height[end])

        return vol