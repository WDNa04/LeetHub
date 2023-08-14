import sys

def findKthLargest(nums, k):
    nums_list = list(map(int,nums.split(',')))
    nums_list.remove(max(nums_list))
    return max(nums_list)

nums = sys.stdin.readline()
k = int(sys.stdin.readline())
print(findKthLargest(nums, k))
