# 剑指Offer.57-2.和为s的连续正数序列

##### 难度：简单

##### 关键词：双指针

##### 链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/

## 题目描述

输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

**示例 1：**

```
输入：target = 9
输出：[[2,3,4],[4,5]]
```

**示例 2：**

```
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
```

**限制：**

- `1 <= target <= 10^5`

## 题目解析

两个指针标示序列的首尾。

## 代码实现

```c++
class Solution {
public:
    vector<vector<int>> findContinuousSequence(int target) {
        vector<vector<int>> result;
        if(target < 3){
            return result;
        }
        int p1 = 1;
        int p2 = 2;
        int sum = p1+p2;
        while(p2 < target && p1 < p2){
            if(sum == target){

                vector<int> tmp;
                for(int i=p1; i<=p2;++i){
                    tmp.emplace_back(i);
                }
                result.emplace_back(tmp);
                ++p2;
                sum += p2;
            }else if(sum > target){
                //太大了，减小p2                
                sum -= p1;
                ++p1;
            }else{
                ++p2;
                sum += p2;
            }
        }
        return result;
    }
};
```

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗：6.7 MB, 在所有 C++ 提交中击败了78.07%的用户

## 题解

