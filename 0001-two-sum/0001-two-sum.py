class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lol = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in lol:
                return[lol[difference], i]
            lol[n] = i
        


        