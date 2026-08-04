class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        saw=set()
        for i in nums:
            if i in saw:
                return True
            saw.add(i)
        return False

            
        