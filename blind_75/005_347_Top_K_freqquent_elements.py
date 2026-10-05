# https://leetcode.com/problems/top-k-frequent-elements/description/

from pathlib import Path
import utils

# ToDo: Implement with heap too

def topKFrequent(nums: list[int], k: int) -> list[int]:
        nums_dict = {}
        freq_dict = {}

        for num in nums:
            freq = 0
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
            
            freq = nums_dict[num]
            if freq>1:
                freq_dict[freq-1].remove(num)

            if freq in freq_dict:
                freq_dict[freq].append(num)
            else:
                freq_dict[freq] = [num]
        
        ret = [] 
        sorted_freq = sorted(freq_dict.keys())
        
        while k>0:
            highest_freq_elements = freq_dict[sorted_freq.pop(-1)]
            for num in highest_freq_elements:
                ret.append(num)
                k-=1
                if k==0:
                    break
        return ret

test_cases = [ [[1,1,1,2,2,3], 2], [[1], 1], [[1,2,1,2,1,2,3,1,3,2], 2], [[-1,-1], 1], [[1,1], 1], [[5,3,1,1,1,3,73,1], 2]]
expected_outputs=[ [1,2], [1], [1,2], [-1], [1], [1,3]]

print(f"\n{Path(__file__).name}")

for (index, test_case) in enumerate(test_cases):
    output = topKFrequent(test_case[0], test_case[1])
    result = utils.Test_Case_Result.Pass.value if output == expected_outputs[index] else utils.Test_Case_Result.Fail.value
    colour = utils.Terminal_Text_Colours.GREEN.value if result == utils.Test_Case_Result.Pass.value else utils.Terminal_Text_Colours.RED.value
    print(f"{colour}{index+1}. {test_case}: output {output} => {result}{utils.Terminal_Text_Colours.RESET.value}")