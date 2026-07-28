class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        flag=False
        while left<=right:
            if nums[left]==target:
                if nums[right]==target:
                    return (left,right)
                    flag=True
                    break
                else:
                    right-=1
            else:
                left+=1
        if flag==False:
            return [-1,-1]


            