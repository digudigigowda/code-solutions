class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.index(c) for c in s] == [t.index(c) for c in t]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna