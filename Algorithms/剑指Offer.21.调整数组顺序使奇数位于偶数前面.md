# 剑指Offer.21.调整数组顺序使奇数位于偶数前面

##### 难度：简单

##### 关键词：双指针

##### 链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/

## 题目描述

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：

```
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
```


提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

双指针。

注意特殊输入：列表全为奇数或全为偶数

## 代码实现

```c++
class Solution {
public:
    vector<int> exchange(vector<int>& nums) {
        int i = 0;
        int j = nums.size()-1;
        while(i < j){
            while(i < j && nums[i] & 1){
                ++i;
            }
            while(i<j && (nums[j] & 1) == 0){
                --j;
            }
            if(j < i){
                break;
            }
            swap(nums[i], nums[j]);
            ++i;
            --j;
            
        }
        return nums;
    }
};
```

执行用时：44 ms, 在所有 C++ 提交中击败了56.14%的用户

内存消耗：18.1 MB, 在所有 C++ 提交中击败了22.19%的用户

## 题解

