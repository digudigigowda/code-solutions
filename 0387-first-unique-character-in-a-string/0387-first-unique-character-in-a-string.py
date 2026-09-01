class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for i,j in enumerate(s):
            if d[j]==1:
                return i
        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna