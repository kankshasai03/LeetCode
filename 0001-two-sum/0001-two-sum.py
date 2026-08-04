class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key={}
        n=len(nums)
        for i in range(n):
            need=target-nums[i]
            if need in key:
                return [i,key[need]]
            else:
                key[nums[i]]=i
        