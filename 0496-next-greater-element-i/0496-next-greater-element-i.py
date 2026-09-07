class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        greater_map = {}

        for num in nums2:
            while stack and stack[-1] < num:
                smaller = stack.pop()
                greater_map[smaller] = num
            stack.append(num)

        return [greater_map.get(x, -1) for x in nums1]
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna