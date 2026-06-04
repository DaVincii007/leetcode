# https://leetcode.com/problems/valid-anagram/description/

def isAnagram(s: str, t: str) -> bool:
    s_dict = {}
    for s_char in s:
        if s_char in s_dict:
            s_dict[s_char] += 1
        else:
            s_dict[s_char] = 1

    for t_char in t:
        if t_char in s_dict:
            if s_dict[t_char] == 1:
                del s_dict[t_char]
            else:
                s_dict[t_char] -= 1
        else:
            return False

    return not s_dict




test_cases=[ ["anagram", "nagaram"], ["rat", "car"] ]

for test_case in test_cases:
    print(isAnagram(test_case[0], test_case[1]))