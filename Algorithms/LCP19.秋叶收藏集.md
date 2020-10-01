

# LCP19.秋叶收藏集

##### 难度：中等

##### 关键词：……

##### 链接：https://leetcode-cn.com/problems/UlBDOe/

## 题目描述

小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

示例 1：

```
输入：leaves = "rrryyyrryyyrr"

输出：2

解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"
```

示例 2：

```
输入：leaves = "ryr"

输出：0

解释：已符合要求，不需要额外操作
```

提示：
3 <= leaves.length <= 10^5
leaves 中只包含字符 'r' 和字符 'y'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/UlBDOe
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

动态规划。

## 代码实现

```c++
class Solution {
public:
        //0: 红、1:黄、2:红
        //测试用例： 空字符串、
      int minimumOperations(string leaves) {
        int n = leaves.length();// 字符串长度
        vector<vector<int>> f(n, vector<int>(3));
        f[0][0] = (leaves[0] == 'y');//此时需要1的替换成本
        f[0][1] = f[0][2] = f[1][2] = INT_MAX;
        for(int i=1;i<n;i++){
            int isYellow = (leaves[i] == 'y' ); //leaves[i]是不是黄色
            int isRed = (leaves[i] == 'r' ); //leaves[i]是不是红色
            f[i][0] = f[i-1][0] + isYellow;//如果是黄色成本需要+1:由黄变成红
            f[i][1] = min(f[i-1][0], f[i-1][1]) + isRed;
            if(i>=2){
                f[i][2] = min(f[i-1][1], f[i-1][2]) + isYellow;
            }

        }
        
        return f[n-1][2];        
    }
};
```

执行用时：688 ms, 在所有 C++ 提交中击败了22.26%的用户

内存消耗：111.6 MB, 在所有 C++ 提交中击败了13.50%的用户

## 题解

