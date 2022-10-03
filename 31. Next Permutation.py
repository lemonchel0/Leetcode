def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 1
    if i == 0:
        return nums.sort()
    while(nums[i] <= nums[i-1]):
        i = i-1
        if i == 0:
            return nums.sort()
    j = i
    k = 0
    while j < len(nums) and nums[i-1] < nums[j]:
        j=j+1
        k = 1
    tmp = nums[j-k]
    nums[j-k] = nums[i-1]
    nums[i-1] = tmp
    nums[i:] = sorted(nums[i:])
    return nums
