# @Author: weirdgiser
# @Time: 2024/9/3
# @Function:
"""
 asduidjklmnn
"""
import sys
from pathlib import Path
from Code.utils.general import perf_profile
sys.path.insert(0, str(Path(__file__).resolve().parent))
from brute import Solution as Solution1
from space import Solution as Solution2
cases = [
    "asduidjklmnn",
    "a",
    "aba",
    "ab",
    "",
    "abba",
    "abababscasedddddaewr",
    "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
]
@perf_profile
def test_solution1(run=10):
    for _ in range(run):
        solution = Solution1()
        for case in cases:
            solution.lengthOfLongestSubstring(case)

@perf_profile
def test_solution2(run=10):
    for _ in range(run):
        solution = Solution2()
        for case in cases:
            solution.lengthOfLongestSubstring(case)

if __name__ == "__main__":
    test_solution1()
    test_solution2()
