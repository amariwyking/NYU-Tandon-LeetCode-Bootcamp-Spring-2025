from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr = 0
        right_ptr = len(numbers) - 1

        while left_ptr < right_ptr:
            sum = numbers[left_ptr] + numbers[right_ptr]

            if sum == target:
                return [left_ptr + 1, right_ptr + 1]
            elif sum < target:
                left_ptr += 1
            else:
                right_ptr -= 1