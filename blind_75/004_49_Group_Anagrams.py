# https://leetcode.com/problems/group-anagrams/description/

import utils

def groupAnagrams(strs:list[str]) -> list[list[str]]:    
    anagram_groups=dict()
    
    for word in strs:
        index_table =[0]*26
        for alphabet in word:
            index_table[ord(alphabet)-97] += 1
        index_table=tuple(index_table)
        if index_table in anagram_groups:
            anagram_groups[index_table].append(word)
        else:
            anagram_groups[index_table] = [word]

    return list(anagram_groups.values())

test_cases = [ ["eat","tea","tan","ate","nat","bat"], [""], ["a"]]
expected_outputs=[ [["bat"],["nat","tan"],["ate","eat","tea"]], [[""]], [["a"]] ]

print(utils.Test_Case_Result.Pass.value)

for (index, test_case) in enumerate(test_cases):
    output = groupAnagrams(test_case)
    result = utils.Test_Case_Result.Pass.value if sorted([sorted(sublist) for sublist in output]) == sorted(sorted([sorted(sublist) for sublist in expected_outputs[index]])) else utils.Test_Case_Result.Fail.value
    colour = utils.terminal_text_colours.GREEN.value if result == utils.Test_Case_Result.Pass.value else utils.terminal_text_colours.RED.value
    print(f"{colour}{index+1}. {test_case}: output {output} => {result}{utils.terminal_text_colours.RESET.value}")