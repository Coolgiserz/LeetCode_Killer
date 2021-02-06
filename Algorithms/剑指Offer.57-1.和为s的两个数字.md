# 剑指Offer.57-1.和为s的两个数字

##### 难度：简单

##### 关键词：数组、双指针

##### 链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/

## 题目描述

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
```

**示例 2：**

```
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
```

**限制：**

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

## 题目解析

### 思路：双指针

## 代码实现

### 实现

```c++
class Solution {
public:
    //利用上数组是递增的信息
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result(2, 0);
        
        int low = 0;
        int high = nums.size()-1;
        while(low < high){
            int sum = nums[low] + nums[high];
            if(sum > target){
                //太大了
                --high;
            }else if(sum < target){
                ++low;
            }else{
                result[0] = nums[low];
                result[1] = nums[high];
                return result;
            }
        }
        return result;
    }
};
```

执行用时：204 ms, 在所有 C++ 提交中击败了96.35%的用户

内存消耗：98.3 MB, 在所有 C++ 提交中击败了81.80%的用户

## 题解

