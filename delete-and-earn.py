def deleteAndEarn(nums: list[int]) -> int:
    nums = [i * nums.count(i) for i in range(1, max(nums) + 1)]
    if len(nums) < 3:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
    listy = [0] * len(nums)
    listy[0] = nums[0]
    listy[1] = nums[1]
    for i in range(2, len(nums)):
        if i > 2:
            listy[i] = nums[i] + max(listy[i-2], listy[i-3])
        else:
            listy[i] = nums[i] + listy[i-2]
    return max(listy[-1], listy[-2])