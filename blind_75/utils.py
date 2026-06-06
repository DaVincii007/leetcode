from enum import Enum, auto, unique

class Terminal_Text_Colours(Enum):
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'

class Test_Case_Result(Enum):
    Pass = 'Passed'
    Fail = 'FAILED'