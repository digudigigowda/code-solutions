class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        k = 0  
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k  

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna