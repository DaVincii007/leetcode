# https://leetcode.com/problems/two-sum/description/

def twoSum(nums: list[int], target: int) -> list[int]:
    nums_dict = {}

    for (index, num) in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [index, nums_dict[complement][0]]

        if num not in nums_dict:
            nums_dict[num] = [index]
        else:
            nums_dict[num].append(index)



test_cases = [ [[2,7,11,15], 9], [[3,2,4], 6], [[3,3], 6] ]

for test_case in test_cases:
    print(twoSum(test_case[0], test_case[1]))
