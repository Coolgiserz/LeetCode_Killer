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

假设$dp[i][j]$为到(i,j)位置处的最大价值，则$dp[i][j]$只与$dp[i-1][j]$和$dp[i][j-1]$相关。

$dp[i][j]=max(dp[i-1][j], dp[i][j-1])+grid[i][j]$

### 思路2: 空间效率优化-采用一维数组保存状态

实际上，没有必要保存第$i-2$行以前的状态，只需要记录第$i-1$行和第$i$行的部分状态即可。

用一个长度为列数的一维数组，从0到j-1位置保存当前行能拿到礼物的最大价值：$dp[i][0]$, $dp[i][1]$, ……, $dp[i][j-1]$,第j到cols-1位置保存前一行cols-j个格子能拿到礼物的最大价值：$dp[i-1][j]$, $dp[i-1][j+1]$, ……, $dp[i-1][cols-1]$

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

### 实现2

```c++
class Solution {
public:
    int maxValue(vector<vector<int>>& grid) {
        int n = grid.size();
        int cols = grid[0].size();
        vector<int> dp(cols, 0);

        for(int i=0;i<n;++i){
            for(int j=0;j<cols;++j){
                int left = 0;
                int up = 0;
                if(i>0){
                    up = dp[j];//(i-1, j)
                }
                if(j>0){
                    left = dp[j-1];//(i, j-1)
                }
                dp[j] = max(left, up)+grid[i][j];
            }
        }
        return dp[cols-1];
    }
};
```

执行用时：4 ms, 在所有 C++ 提交中击败了99.66%的用户

内存消耗：8.9 MB, 在所有 C++ 提交中击败了93.82%的用户

## 题解

