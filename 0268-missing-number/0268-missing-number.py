class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        d=n*(n+1)//2
        a=sum(nums)
        return d-a

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna