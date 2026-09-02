class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        q=list(t)
        for i in s:
            q.remove(i)
        return(q[0])
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna