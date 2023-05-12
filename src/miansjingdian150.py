# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。
# 为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
from typing import List

# 我的题解
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == 0:
            nums1 = nums2
        elif len(nums2) == 0:
            nums1 = nums1
        elif len(nums1) == 0 and len(nums2) == 0:
            nums1 = nums1
        else:
            for i in nums2:
                nums1[m] = i
                m += 1
            nums1.sort()
        return nums1

nums1 = input()
m = int(input())
nums2 = input()
n = int(input())
num1 = Solution.merge(nums1,m,nums2,n)
print(num1)