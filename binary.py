#
#

'binary'

__author__ = 'hjkruclion'

import sys

def read_int():
    return list(map(int, sys.stdin.readline().split()))

class Solution:
    def b_b(self, m, x, b):
        l = 0
        r = m
        while(l < r):
            mid = (l + r) // 2
            if b[mid] <= x:
                l = mid + 1
            else:
                r = mid
        return r - 1 + 1
    def b_a(self, n, m, key, a, b):
        l = 0
        r = n
        while(l < r):
            mid = (l + r) // 2
            res = mid + 1 + self.b_b(m, a[mid], b)
            if res <= key:
                l = mid + 1
            else:
                r = mid
        return r - 1

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a = nums1
        b = nums2
        n = len(a)
        m = len(b)
        key = (n + m + 1) // 2
        x = self.b_a(n, m, key, a, b)
        # print(x)
        num_x = x - 0 + 1
        num_y = key - num_x
        if x < 0:
            L = b[num_y - 1]
        else:
            L = a[x]
            if num_y - 1 >= 0:
                L = max(a[x], b[num_y - 1])
        if (n + m) % 2 == 1:
            return L
        else:
            Ra = x + 1
            Rb = num_y - 1 + 1
            if Ra >= n:
                R = b[Rb]
            elif Rb >= m:
                R = a[Ra]
            else:
                R = min(a[Ra], b[Rb])
            return (L + R) / 2

a = read_int()
b = read_int()
c = Solution()
print(c.findMedianSortedArrays(a, b))