# 剑指Offer.10-2.青蛙跳台阶问题

##### 难度：简单

##### 关键词：递归

##### 链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof

## 题目描述

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

```
输入：n = 2
输出：2
```

示例 2：

```
输入：n = 7
输出：21
```

示例 3：

```
输入：n = 0
输出：1
```

提示：

- 0 <= n <= 100

  注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

本质上是斐波那契数列问题

## 代码实现

```c++
class Solution {
public:
    //本质上是斐波那契数列问题
    int numWays(int n) {
        vector<int> dp(n+2, 0);
        dp[0] = 1;
        dp[1] = 1;
        if(n<2){
            return dp[n];
        }
        for(int i=2; i<n+1; ++i){
            dp[i] = dp[i-1]+dp[i-2];
            dp[i] = dp[i] % 1000000007;
        }
        return dp[n];
    }
};
```

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗：6.6 MB, 在所有 C++ 提交中击败了5.11%的用户

## 题解

### 为什么**大数阶乘，大数的排列组合**一般要求模1000000007？

取模原因是为了防止大数越界，当一个问题只对答案的正确性有要求，而不在乎答案的数值，可能会需要将取值很大的数通过求余变小。

1000000007是一个质数，对于int的数值范围而言，对其取模不会溢出也不会冲突。

参考资料：https://www.zhihu.com/question/49374703