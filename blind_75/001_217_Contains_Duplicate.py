# https://leetcode.com/problems/contains-duplicate/description/
from pathlib import Path

def containsDuplicate(nums: list[int]) -> bool:
    nums_set = set()
    for num in nums:
        if num in nums_set:
            return True
        else:
            nums_set.add(num)
    return False




test_cases =[ [1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2] ]

print(f"\n{Path(__file__).name}")
for test_case in test_cases:
    print(containsDuplicate(test_case))
