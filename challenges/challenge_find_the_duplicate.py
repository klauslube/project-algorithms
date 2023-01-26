def find_duplicate(nums):
    nums.sort()

    if len(nums) <= 1:
        return False

    for index in range(len(nums) - 1):
        if not isinstance(nums[index], int) or nums[index] < 0:
            return False

        elif nums[index] == nums[index + 1]:
            return nums[index]
    return False
