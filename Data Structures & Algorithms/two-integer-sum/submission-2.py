class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if (target - nums[i]) == nums[j]:
    #                 return [i,j]
    #     return [0,0]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dict = {}
        for index,item in enumerate(nums):
                result_dict.update({item: index})
        for index,item in enumerate(nums):
                if (target - item) in result_dict and index != result_dict[target-item]:
                    return [index, result_dict[target-item]]
        return []