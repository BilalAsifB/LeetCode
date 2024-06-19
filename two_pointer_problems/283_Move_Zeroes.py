class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1 = 0
        p2 = 1
        end = len(nums) - 1

        while p2 <= end:
            if nums[p1] == 0:
                if nums[p2] == 0:
                    while p2 != end and nums[p2] == 0:
                        p2 += 1
                nums[p1] = nums[p2]
                nums[p2] = 0
            if p2 + 1 <= end:
                p1 += 1
                p2 += 1
            else:
                break