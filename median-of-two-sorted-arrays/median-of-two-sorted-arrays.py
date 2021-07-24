class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tot = nums1 + nums2
        tot.sort()
        if len(tot) == 0 :
            return 0
        if len(tot)%2 == 1 :
            return tot[int(len(tot)/2)]
        else :
            return ( tot[int((len(tot)/2)-1)] + tot[int(len(tot)/2)] )/2