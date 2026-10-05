# https://leetcode.com/problems/product-of-array-except-self/description/
from pathlib import Path
import utils

def productExceptSelf(nums: list[int]) -> list[int]:
    left_prod = [1]*len(nums)
    right_prod = [1]*len(nums)
    prod_except_self=[1]*len(nums)

    for (index, num) in enumerate(nums):
        if index !=0:
            left_prod[index] = left_prod[index-1] * nums[index-1]
            right_prod[-1-index] = right_prod[-index] * nums[-index]

    for index in range(len(nums)):
        prod_except_self[index] = right_prod[index] * left_prod[index]
    return prod_except_self

test_cases = [ [1,2,3,4], [-1,1,0,-3,3] ]
expected_outputs = [ [24,12,8,6], [0,0,9,0,0] ]

for (index, test_case) in enumerate(test_cases):
    output = productExceptSelf(test_case)
    result = utils.Test_Case_Result.Pass.value if output == expected_outputs[index] else utils.Test_Case_Result.Fail.value
    colour = utils.Terminal_Text_Colours.GREEN.value if result == utils.Test_Case_Result.Pass.value else utils.Terminal_Text_Colours.RED.value
    print(f"{colour}{index+1}. {test_case}: output {output} => {result}{utils.Terminal_Text_Colours.RESET.value}")