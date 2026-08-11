class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        x = len(nums1) - 1
        while x >= 0:
            if i >=0 and j < 0:
                nums1[x] = nums1[i]
                i -= 1
            elif j >= 0 and i < 0:
                nums1[x] = nums2[j]
                j -= 1
            elif nums1[i] > nums2[j]:
                nums1[x] = nums1[i]
                i -= 1
            else:
                nums1[x] = nums2[j]
                j -= 1
            x -= 1
            

