class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[p],nums[i]=nums[i],nums[p]
                p+=1
                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna