class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = float('inf')
        ans = 0

        for p in prices:
            if p < low:
                low = p
            elif p - low > ans:
                ans = p - low

        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna