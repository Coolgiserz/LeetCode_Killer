# 剑指Offer.42.连续子数组的最大和

##### 难度：简单

##### 关键词：分治算法、动态规划

##### 链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/

## 题目描述

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:

```
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```


提示：

- 1 <= arr.length <= 10^5
- -100 <= arr[i] <= 100
  注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

最为简单的想法是计算所有的连续子数组的和，从而得到最大和，这种方法需要的时间复杂度为$O(N^2)$。

还可以考虑使用动态规划的思想。记$f(i)$为数组中到索引i为止的连续子数组的最大和，如此则有:

当$f(i-1)>0$时，$f(i)=f(i-1)+nums[i]$；当$f(i-1)<0$时，$f(i)=nums[i]$。



## 代码实现

### 实现1: 动态规划

```c++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        if( n == 1){
            return nums[0];
        }
        vector<int> dp(n, 0);
        dp[0] = nums[0];
        int maxSum = -INT_MAX;
        for(int i=0;i<n;++i){
            if(i>0){
                if(dp[i-1]<0){
                    dp[i] = nums[i];
                }else{
                    dp[i] = dp[i-1] + nums[i];
                }
            }
            
            if(dp[i]>maxSum){
                maxSum = dp[i];
            }
        }
        return maxSum;
    }
};
```

执行用时：28 ms, 在所有 C++ 提交中击败了91.23%的用户

内存消耗：22.9 MB, 在所有 C++ 提交中击败了43.51%的用户

### 实现2

比实现1更节省空间，不需要使用大小为n的数组存储历史状态，只用1个curSum变量存储到当前索引的连续子数组最大和。

```c++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        if( n == 1){
            return nums[0];
        }
        int curSum = nums[0];
        int maxSum = -INT_MAX;

        for(int i=0;i<n;++i){
            if(i>0){
                if(curSum<0){
                    curSum = nums[i];
                }else{
                    curSum += nums[i];
                }
            }
            
            if(curSum>maxSum){
                maxSum = curSum;
            }
        }
        return maxSum;
    }
};
```

执行用时：24 ms, 在所有 C++ 提交中击败了94.90%的用户

内存消耗：22.4 MB, 在所有 C++ 提交中击败了92.91%的用户

## 题解

