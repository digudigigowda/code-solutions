class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        most_common = max(set(nums), key=nums.count)

        return most_common 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna