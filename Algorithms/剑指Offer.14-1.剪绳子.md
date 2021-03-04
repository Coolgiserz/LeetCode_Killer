# 剑指Offer.14-1.剪绳子

##### 难度：中等

##### 关键词：数学、动态规划

##### 链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof/

## 题目描述

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 $m$ 段（$m$、$n$都是整数，$n>1$并且$m>1$），每段绳子的长度记为 $k[0],k[1]...k[m-1]$ 。请问$ k[0]*k[1]*...*k[m-1]$ 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

```
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
```

**示例 2:**

```
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
```

提示：

- 2 <= n <= 58

注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路：动态规划

自顶向下还是自底向上？

问题可以变成$cuttingRope(n)=max(cuttingRope(i)*cuttingRope(n-i))$，但如果自顶向下计算的话可以预见会有很多重复计算。

可以考虑通过自底向上减少重复计算。

## 代码实现

```c++
class Solution {
public:
    int cuttingRope(int n) {
        if(n==2){
            return 1;
        }else if(n==3){
            return 2;
        }
        vector<int> products(n+1);
        products[0] = 0;
        products[1]= 1;
        products[2] = 2;
        products[3] = 3;
        int maxvalue = 0;
        for(int i=4; i<=n;++i){
            for(int j=1;j<=i/2;++j){
                int p = products[j] * products[i-j];
                if(maxvalue < p){
                    maxvalue = p;
                }

                products[i] = maxvalue;

            }
        }
        return products[n];

    }
};
```

执行用时：4 ms, 在所有 C++ 提交中击败了23.82%的用户

内存消耗：6 MB, 在所有 C++ 提交中击败了74.15%的用户

## 题解

