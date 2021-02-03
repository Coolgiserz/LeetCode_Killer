# 剑指Offer.51.数组中的逆序对

##### 难度：困难

##### 关键词：分治

##### 链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/

## 题目描述

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。 

示例 1:

```
输入: [7,5,6,4]
输出: 5
```


限制：

```
0 <= 数组长度 <= 50000
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路1: 暴力

双重循环。

### 思路2: 

分而治之。将数组拆分成两部分A和B，分别在A、B内部统计逆序对res1，然后对A、B排序后统计A的元素和B的元素之中有多少逆序对res2。最终结果就是res1+res2.

所以，关键问题为：

- 如何统计A内或B内有多少逆序对？
- 如何统计子数组A和B之间有多少逆序对？

## 代码实现

### 实现1

```c++
class Solution {
public:
    int reversePairs(vector<int>& nums) {
        if(nums.size()<2){
            return 0;
        }
        int result = 0;
        for(int i=0;i<nums.size()-1;++i){
            for(int j=i+1;j<nums.size();++j){
                if(nums[i]>nums[j]){
                    ++result;
                }
            }
        }
        return result;
    }
};
```

[超出时间限制](https://leetcode-cn.com/submissions/detail/143485271/)

### 实现2

```c++
class Solution {
public:
    int reversePairs(vector<int>& nums) {
        if(nums.size()<2){
            return 0;
        }
        vector<int> copy(nums.size(), 0);
        for(int i=0;i<nums.size();++i){
            copy[i] = nums[i];
        }
        return reversepaircore(nums, copy, 0, nums.size()-1);
    }

    int reversepaircore(vector<int>& nums, vector<int>& copy, int start, int end){
        if(start == end){
            copy[start] = nums[start];
            return 0;
        }
        int length = (end-start)/2; //数组长度
        int left = reversepaircore(copy, nums, start, start+length);
        int right = reversepaircore(copy, nums, start+length+1, end);

        int count = 0;
        int i =start+length;
        int j = end;
        int indexCopy = end;
        while(i>=start && j>=start+length+1){
            if(nums[i]>nums[j]){
                copy[indexCopy--] = nums[i--];
                count += j-start-length;
            }else{
                copy[indexCopy--] = nums[j--];
            }
        }
        while(i>=start){
            copy[indexCopy--] = nums[i--];
        }
			//假设能找到的逆序对都找了，此时B子数组（已排序）剩余元素是整个数组中最小的元素
        while(j>=start+length+1){
            copy[indexCopy--] = nums[j--];
        }
      //得到的copy数组是对nums排序后的结果
        return count + left + right;
    }
};
```

执行用时：168 ms, 在所有 C++ 提交中击败了99.06%的用户

内存消耗：43.3 MB, 在所有 C++ 提交中击败了84.48%的用户

## 题解

