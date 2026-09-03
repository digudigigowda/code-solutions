class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
       
        n=len(nums)
        counts=[0]*(n+1)
        for num in nums:
            counts[num]=1
        return [i for i in range(1,n+1) if counts[i]<1]
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna