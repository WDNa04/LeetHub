import sys

def twoSum(self, nums, target):
    for i in range(len(nums)):
        for k in range(i+1, len(nums)):
            if nums[i] + nums[k] == target:
                return [i,k]

nums = list(map(int,sys.stdin.readline().split(',')))
target = int(sys.stdin.readline())
print(twoSum('self',nums,target))
