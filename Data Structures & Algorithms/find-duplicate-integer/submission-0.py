class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        fast = 0   # fast
        slow = 0   # slow
        n = len(nums) - 1
        while True: 
            
            slow = nums[slow]   # move 1 step, slow = slow.next
            fast = nums[nums[fast]] # move 2 steps, fast = fast.next.next

            if slow == fast: # if circle exisit, there is a duplicate and we break out
                break 

        # The distance from the start of the list to the cycle entrance is exactly equal to the distance from the
        # intersection point to the cycle entrance.
        slow2 = 0 # start from begining
        while slow != slow2: # move until they meet a duplicate
            slow = nums[slow]
            slow2 = nums[slow2] 

        return slow