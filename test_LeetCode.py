def twoSum(nums, target):
    for i in range(len(nums)):
        for k in range(i+1, len(nums)):
            if nums[i] + nums[k] == target:
                return [i,k]

import sys
nums = sys.stdin.readline()
target = int(sys.stdin.readline())
print(twoSum(nums, target))