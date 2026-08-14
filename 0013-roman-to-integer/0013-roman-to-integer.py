class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        t=0
        p=0
        for i in reversed(s):
            c=d[i]
            if c<p:
                t-=c
            else:
                t+=c
            p=c
        return t
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna