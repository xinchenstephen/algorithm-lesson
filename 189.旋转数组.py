#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
###法1:使用环状替换
# 总体思路：把每个元素（同学）直接挪到新的位置（座位）上去，每隔k个元素
# 挪动，因为这样可以只留一个备用位置记录元素即可。
# 法:先挪i%k==0的序列，挪完挪i%k==1,一直挪到i%k又等于0(或者所有元素都挪过一遍)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        count = 0
        start = -1
        n = len(nums)
        while(count<n):
            start += 1
            current = start
            prev = nums[current]
            while (True):
                next = (current + k)%n
                tem = nums[next]
                nums[next] = prev
                prev = tem
                current = next 
                count += 1
                if (current == start):
                    break
            #挪动i%k==0的序列
                #每次挪动count += 1
            
        
# @lc code=end

