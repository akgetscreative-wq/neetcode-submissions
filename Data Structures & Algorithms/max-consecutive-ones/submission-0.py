class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        i = 0
        count=0
        count1 = 0
        

        for i in range(len(nums)):
            if nums[i]==1:
                count1 +=1
                if count1>count:
                    count=count1
            else:
                    count1=0
            

        return count