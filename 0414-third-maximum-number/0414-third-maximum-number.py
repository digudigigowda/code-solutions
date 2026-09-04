class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        q=sorted(set(nums),reverse=True)
        return q[2] if len(q)>=3 else q[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna