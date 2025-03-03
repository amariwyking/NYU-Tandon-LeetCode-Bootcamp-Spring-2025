from typing import List


def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_dict = {
            0: 0,
            1: 0,
            2: 0,
        }

        for num in nums:
            num_dict[num] = num_dict[num] + 1

        idx = 0
        for num in num_dict.keys():
            while num_dict[num]:
                nums[idx] = num
                num_dict[num] = num_dict[num] - 1

                idx += 1