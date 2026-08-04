class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """left=0
        n=len(nums)
        right=n-1
        while left<right:
            nums[left]*=nums[left]
            nums[right]*=nums[right]
            
            if nums[left]>nums[right]:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
            else:
                right-=1
                
        return nums"""
        n=len(nums)
        ans=[0]*n
        ind=-1
        i,j=0,n-1
        while i<=j:
            if nums[i]*2>nums[j]*2:
                ans[ind]=nums[i]**2
                i+=1
            else:
                ans[ind]=nums[j]**2
                j-=1
            ind-=1
            ans.sort()
        return ans
        