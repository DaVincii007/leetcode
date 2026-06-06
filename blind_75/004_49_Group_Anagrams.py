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
