class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna