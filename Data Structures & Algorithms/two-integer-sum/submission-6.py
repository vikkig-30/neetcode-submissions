class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                return [nums.index(target-nums[i]),i]
                """
                if i < nums.index(target-nums[i]):
                    return [i,nums.index(target-nums[i])]
                else:
                    return [nums.index(target-nums[i]),i]
                """
            hashmap[nums[i]] = i
        

            

        