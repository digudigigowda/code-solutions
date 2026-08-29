class Solution:
    def reverseVowels(self, s: str) -> str:
        v=[c for c in s if c in "aeiouAEIOU"]
        return "".join(c if c not in "aeiouAEIOU"else v.pop() for c in s ) 
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna