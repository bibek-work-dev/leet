class Arrays:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        checker = dict()
        for index, value in enumerate(nums):
            if (target-value) in checker:
                return [checker[target-value],index]
            else:
                checker[value] = index
        return []
    

array = Arrays()
print(array.twoSum([2,7,11,15], 9))
print(array.twoSum([3,2,4], 6))
