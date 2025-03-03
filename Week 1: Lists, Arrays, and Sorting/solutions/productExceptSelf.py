def productExceptSelf(self, nums):
    product = None

    left_products = []

    for idx in range(len(nums)):
        if idx == 0:
            product = 0
        elif idx == 1:
            product = nums[idx - 1]
        else:
            product *= nums[idx - 1]

        left_products.append(product)

    right_products = []

    for idx in reversed(range(len(nums))):
        if idx == len(nums) - 1:
            product = 0
        elif idx == len(nums) - 2:
            product = nums[len(nums) - 1]
        else:
            product *= nums[idx + 1]

        right_products.append(product)

    right_products.reverse()

    answers = []

    for idx in range(0, len(nums)):
        if idx == 0:
            answers.append(right_products[idx])
        elif idx == len(nums) - 1:
            answers.append(left_products[idx])
        else:
            answers.append(
                left_products[idx] * right_products[idx]
            )

    return answers
        