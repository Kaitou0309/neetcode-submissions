class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(nums1) + len(nums2)
        half = total // 2 # tells how many values needs to be on the left
        
        l, r = 0, len(A) # count elements, not idx

        while l <= r: 
            i = (l + r) // 2    # i = How many items we take from A
            j = half - i        # j = How many items we take from B

            # GET INDICES 
            # If i=0, Left A is empty (-inf). If i=len(A), Right A is empty (+inf).
            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < len(A) else float('inf')

            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright: 

                if total % 2: 
                    return min(Aright, Bright)
                else: 
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright: 
                r = i - 1
            else: 
                l = i + 1
        