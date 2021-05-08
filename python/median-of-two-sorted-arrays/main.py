from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        nums1: length=m
        nums2: length=n
        time complexity: O(log (m+n))
        """
        joined = nums1 + nums2
        sorted_array = sorted(joined) # TODO: Do I have to implement quick sort?
        array_length = len(sorted_array)

        # time complexity below is O(n+m)
        if array_length % 2 == 0:
            # Even: [0, 1, 2, 3] #  4//2 = 2
            second_index = array_length // 2
            return (sorted_array[second_index-1] + sorted_array[second_index]) / 2
        else:
            # Odd: [0, 1, 2, 3, 4] # 5//2 = 2
            index = array_length // 2
            return sorted_array[index]


def t():
    s = Solution()

    nums1 = [0, 0]
    nums2 = [0, 0]
    r = s.findMedianSortedArrays(nums1, nums2)
    print(r)

t()