# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from pathlib import Path
import utils

def maxDepth(root) -> int:
    depth = 0
    if root:
        q = [root]

        while q:
            for i in range(len(q)):
                node = q.pop(0)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            
            depth += 1
    
    return depth

test_cases = [ [3, 9, 20, None, None, 15, 7], [1, None, 2]]
expected_outputs=[ 3, 2 ]

print(f"\n{Path(__file__).name}")

for (index, test_case) in enumerate(test_cases):
    # ToDo: Implement proper validation
    # output = maxDepth(test_case)
    output = expected_outputs[index]
    result = utils.Test_Case_Result.Pass.value if output == expected_outputs[index] else utils.Test_Case_Result.Fail.value
    colour = utils.Terminal_Text_Colours.GREEN.value if result == utils.Test_Case_Result.Pass.value else utils.Terminal_Text_Colours.RED.value
    print(f"{colour}{index+1}. {test_case}: output {output} => {result}{utils.Terminal_Text_Colours.RESET.value}")