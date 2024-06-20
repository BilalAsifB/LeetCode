class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        start = 0
        end = len(height) - 1

        while start < end:
            if height[start] > height[end]:
                vol = (end - start) * height[end]
                end -= 1
            else:
                vol = (end - start) * height[start]
                start += 1
            if vol > max:
                max = vol
        return max