class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1_dict = {}
        nums2_dict = {}

        for n in nums1:
            nums1_dict[n] = True
        
        for n in nums2:
            if n in nums1_dict:
                return n
        
        return -1   