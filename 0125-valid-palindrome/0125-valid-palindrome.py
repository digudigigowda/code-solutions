class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=""
        for i in s:
            if i.isalnum():
                c=c+i.lower()
        c=c[:]==c[::-1]
        return(c)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna