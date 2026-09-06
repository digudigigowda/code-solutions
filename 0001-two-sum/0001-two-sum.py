class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:

       d={}
       for i in range(len(n)):
           c=t-n[i]
           if c in d:
              return (d[c],i)
           d[n[i]]=i



        



        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna