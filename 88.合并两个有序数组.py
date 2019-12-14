#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
#思路1：倒序 搞两个指针指向num1 和num2的末尾，在搞一个指向nums1空间末尾，
#从大向小比
##时间复杂度O(N)
##空间复杂度O(N)
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = len(nums1[0:3])
n = len(nums2)


def merge(nums1, m, nums2, n): 
    """
    Do not return anything, modify nums1 in-place instead.
    """
    end1 = m - 1 
    end2 = n - 1
    end  = m + n -1
    while(end2>=0 and end1>=0):
        if (nums1[end1]>nums2[end2]):
            nums1[end] = nums1[end1]
            end1 -= 1
        else:
            nums1[end] = nums2[end2]
            end2 -= 1
        end -= 1
    if (end2!=0):
        nums1 [0:end2+1] = nums2 [0:end2+1]
# @lc code=

merge(nums1, m, nums2, n)
print(nums1)

