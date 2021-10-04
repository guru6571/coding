class Solution(object):
    def twoSum(self, nums, target):
        temp = nums
        for i in range(0 , nums.length):
            FirstNum = temp.pop(i)
            for val in temp:
                if (val+FirstNum==target):
                    return [FirstNum,val]
            temp = nums
        
        