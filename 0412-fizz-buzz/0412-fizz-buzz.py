class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        p=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                p.append("FizzBuzz")
            elif i%3==0:
                p.append("Fizz")
            elif i%5==0:
                p.append("Buzz")
            else:
                p.append(str(i))
        return p
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna