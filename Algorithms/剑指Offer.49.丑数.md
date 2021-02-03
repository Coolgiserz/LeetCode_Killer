# 剑指Offer.49.丑数

##### 难度：中等

##### 关键词：数学

##### 链接：https://leetcode-cn.com/problems/chou-shu-lcof/

## 题目描述

我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

示例:

```
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
```

说明:  

1. 1 是丑数。
2. n 不超过1690。

注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chou-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路1：暴力

通过暴力的手段判断每一个数是否是丑数，直到找到n个丑数为止。

这样做的缺点是不管是丑数还是非丑数都要进行判断，而且判断一个数是否是丑数需要多次除法运算和取模运算，效率较低。

### 思路2: 利用丑数的性质

直接考虑：如何按顺序生成下一个丑数？

由于丑数只包含质因子2、3、5，所以下一个丑数必定是在现有丑数的基础上乘以2、3、5的结果中的一个，且比现有所有丑数大。实际上，如果记现有丑数中最大的数为M，则下一个丑数一定是现有丑数分别乘以2、3、5之后比M大的第一个数。

## 代码实现

```c++
class Solution {
public:
    
    int nthUglyNumber(int n) {
        if(n<=0){
            return 0;
        }
        int index = 0; //记录当前生成的丑数的索引
        int *uglys = new int[n];
        uglys[index] = 1;
        ++index;
        int m2 = 0;
        int m3 = 0;
        int m5 = 0;
        
        while(index < n){
            uglys[index] = min({uglys[m2]*2, uglys[m3]*3, uglys[m5]*5});
            while(uglys[m2]*2<=uglys[index]){
                ++m2;
            }
            while(uglys[m3]*3<=uglys[index]){
                ++m3;
            }
            while(uglys[m5]*5<=uglys[index]){
                ++m5;
            }

            ++index;
        }
        return uglys[n-1];
    }
};
```

执行用时：8 ms, 在所有 C++ 提交中击败了88.06%的用户

内存消耗：7.5 MB, 在所有 C++ 提交中击败了73.88%的用户

## 题解

