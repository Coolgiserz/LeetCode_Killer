# 剑指Offer.47.礼物的最大价值

##### 难度：中等

##### 关键词：动态规划

##### 链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/

## 题目描述

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:

```
输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
```

提示：

- `0 < grid.length <= 200`
- `0 < grid[0].length <= 200`

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

动态规划的思路

### 思路1: 采用二维辅助数组来保存状态

## 代码实现

### 实现1

```c++
class Solution {
public:
    int maxValue(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> dp(n, vector<int>(grid[0].size(), 0));
        dp[0][0] = grid[0][0];
        for(int i=1;i<n;++i){
            dp[i][0] = dp[i-1][0]+grid[i][0];
        }

        for(int j=1;j<grid[0].size();++j){
            dp[0][j] = dp[0][j-1]+grid[0][j];
        }
        for(int i=1;i<n;++i){
            for(int j=1;j<grid[0].size();++j){
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])+grid[i][j];
            }
        }
        return dp[n-1][grid[0].size()-1];
    }
};
```

执行用时：4 ms, 在所有 C++ 提交中击败了99.66%的用户

内存消耗：9.2 MB, 在所有 C++ 提交中击败了86.26%的用户

## 题解

