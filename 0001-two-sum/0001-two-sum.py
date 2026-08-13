class Solution:
    def twoSum(self, n: List[int], p: int) -> List[int]:
        for i in range (len(n)-1):
            for j in range (i+1,len(n)):
                if n[i]+n[j]==p:
                    return[i,j]

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna