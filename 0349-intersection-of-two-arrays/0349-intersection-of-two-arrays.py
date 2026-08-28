class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=[]
        nu1=set(nums1)
        nu=set(nums2)
        for n in nu:
            if n in nu1:
                n1.append(n)
        return n1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna