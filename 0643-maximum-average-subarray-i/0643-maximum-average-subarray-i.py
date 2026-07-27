class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowsum=sum(nums[:k])
        maxi=windowsum
        for i in range(k,len(nums)):
            windowsum=windowsum-nums[i-k]+nums[i]
            maxi=max(windowsum,maxi)
        return maxi/k
        