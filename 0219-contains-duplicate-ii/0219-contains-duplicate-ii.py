class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s={}
        for i,num in enumerate(nums):
            if num in s and i-s[num]<=k:
                return True
            s[num]=i
        return False
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna