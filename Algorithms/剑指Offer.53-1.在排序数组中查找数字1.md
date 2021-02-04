# 剑指Offer.53-1.在排序数组中查找数字1

##### 难度：简单

##### 关键词：二分查找

##### 链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof

## 题目描述

统计一个数字在排序数组中出现的次数。

示例 1:

```
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
```

示例 2:

```
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
```


限制：

0 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路1: 经典二分查找

不足：由于找到中间的元素后还需要往两边搜索，所以该“二分搜索”实际上复杂度为O(N)，其并没有利用数组是【排序的这一信息。

### 思路2: 改进的二分查找

由于数组是排序的，所以若target出现在数组中，其一定是连续出现。可以：

1. 先找到target第一次出现的位置first
2. 再找到target最后一次出现的位置last
3. 计算得到target出现次数：last-first

### 测试用例

```
[5,7,7,8,8,10]
8
[5,7,7,8,8,8,10]
8
[5,7,7,8,8,8,8,8,8]
8
[8,8,8,8,8,8,8,8]
8
[1]
1
[5,7,7,8,8,10]
6
```



## 代码实现

### 实现1: 经典二分查找

```c++
class Solution {
public:
     //法一： 二分查找，但最差的情况还是O(n)

     //法二： 改进二分查找的对象
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if(n<=0){
            return 0;
        }
        
        int start = 0;
        int end = n-1;
        int middle = (end + start) >> 1;//位运算实现平分

        while(start<=end){
            if(nums[middle]<target){
                //往右边找
                start = middle + 1;
            }else if(nums[middle]>target){
              //往左边查找
                end = middle - 1;
            }else{
                //找到
                int i = middle;
                while(i>=1 && nums[i-1]==nums[middle]){
                    --i;
                }
                int j = middle+1;
                while(j<=end && nums[j]==nums[middle]){
                    ++j;
                }
                return j-i;
            }
            middle = (end+start) >> 1;
        }
        return 0;
    }
};
```

执行用时：8 ms, 在所有 C++ 提交中击败了95.78%的用户

内存消耗：12.9 MB, 在所有 C++ 提交中击败了86.98%的用户

### 实现2

```c++
class Solution {
public:
     //法一： 二分查找，但最差的情况还是O(n)

     //法二： 改进二分查找的对象
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if(n<=0){
            return 0;
        }
        int first = getFirstIndex(nums, target);
        int last = getLastIndex(nums, target);
        if(first > -1){
            return last-first+1;
        }else{
            return 0;
        }
        
    }

    int getFirstIndex(vector<int>& nums, int target){
        int start = 0;
        int end = nums.size()-1;
        int middle = (start + end) >> 1;
        while(start<=end){
            if(nums[middle]<target){
                start = middle+1;
            }else if(nums[middle]>target){
                end = middle - 1;
            }else{
                if(middle==0 || nums[middle-1]!=target){
                     return middle;
                }else{
                    end = middle - 1;
                }

            }
            middle = (start + end) >> 1;
        }
        return -1;
    }

    int getLastIndex(vector<int>& nums, int target){
        int start = 0;
        int end = nums.size()-1;
        int middle = (start + end) >> 1;
        while(start<=end){
            if(nums[middle]<target){
                start = middle+1;
            }else if(nums[middle]>target){
                end = middle - 1;
            }else{
                if(middle==nums.size()-1 || nums[middle+1]!=target){
                     return middle;
                }else{
                    start = middle + 1;
                }

            }
            middle = (start + end) >> 1;

        }
        return -1;
    }
        
       
};
```

执行用时：8 ms, 在所有 C++ 提交中击败了95.78%的用户

内存消耗：12.8 MB, 在所有 C++ 提交中击败了94.62%的用户

## 题解

