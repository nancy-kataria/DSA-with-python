class Solution():
    def twoSum(self, nums, target):
        hashMap=dict()
        
        for i in range(len(nums)):
            # next number should be equal to complement
            if nums[i] in hashMap:
                return [i, hashMap[nums[i]]]
            complement = target - nums[i]
            # store complement's index in hash
            hashMap[complement] = i

two_sum = Solution()
print(two_sum.twoSum([2,7,11,15],9))
print(two_sum.twoSum([3,2,4], 6))
print(two_sum.twoSum([3,3], 6))
