# 剑指Offer.39.数组中出现次数超过一半的数字

##### 难度：简单

##### 关键词：位运算、分治算法

##### 链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/

## 题目描述

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

```
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
```


限制：

1 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路1: 暴力思路

哈希表统计数字出现次数，大于一半的则返回。该方法时间复杂度为O(N), 额外空间复杂度为O(N),N为数组大小

###思路2: 先排序

仔细思考， 数组中出现次数超过一半的数字一定是数组的中位数，也就是说只要数组中确实有出现次数超过一半的数字，只需要对数组排序然后返回数组中间的数字即可。

排序耗费时间O(NlogN), 空间O(1)

### 思路3: 分治法

每次从中随机选一个基准元素，然后将数组划分成2部分，其中一部分的元素都比基准小，另一部分元素都比基准大；

然后对于分开的两部分采用同样的操作。



## 代码实现

### 实现2: 先排序

```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        return nums[n/2];
    }
};
```

执行用时：12 ms, 在所有 C++ 提交中击败了99.72%的用户

内存消耗：18.3 MB, 在所有 C++ 提交中击败了92.93%的用户

### 实现3: 分治

#### 实现版本1

```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int low = 0;
        int high = nums.size()-1;    
        int index = 0;
          // high == low,说明只有一个元素
        return quick(nums, 0, high, nums.size()/2);
    }
    int quick(vector<int>& nums, int low, int high, int middle){
        int index = partion(nums, low, high);
        if(index == middle){
            return nums[index];
        }else if(index > middle){
            return quick(nums, low, index-1, middle);
        }else{
            return quick(nums, index+1, high, middle);
        }
        return nums[index];
    }

    int partion(vector<int>& nums, int low, int high) {
        int pivot = nums[low];
        while (low < high) {
            while (low < high && nums[high] >= pivot) {
            --high;
            }
            nums[low] = nums[high];
            while (low < high && nums[low] <= pivot) {
            ++low;
            }
            nums[high] = nums[low];
        }
        nums[low] = pivot;
        return low;
    }
};
```

对于超长的测试用例会超时

#### 实现版本2

```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int low = 0;
        int high = nums.size()-1;    
        int index = 0;
          // high == low,说明只有一个元素
        return quick(nums, 0, high, nums.size()/2);
    }
    int quick(vector<int>& nums, int low, int high, int middle){
        int index = partion(nums, low, high);
        if(index == middle){
            return nums[index];
        }else if(index > middle){
            return quick(nums, low, index-1, middle);
        }else{
            return quick(nums, index+1, high, middle);
        }
        return nums[index];
    }

    int partion(vector<int>& a, int left, int right) {
        int i=left;
        int j=right+1;
        int pivot=a[left];
        while(true)
        {
            while(i<right && a[++i]<pivot) {}
            while(j>0 && a[--j]>pivot)     {}
            if(i>=j)
            {
                break;
            }
            else
            {
                swap(a,i,j);
            }
        }
        swap(a,left,j);
        return j;
    }
    void swap(vector<int>&  a,int i,int j)
    {
        int temp=a[j];
        a[j]=a[i];
        a[i]=temp;
    }
};
```

执行用时：16 ms, 在所有 C++ 提交中击败了98.85%的用户

内存消耗：18.2 MB, 在所有 C++ 提交中击败了97.22%的用户

#### 实现版本3

```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int low = 0;
        int high = nums.size()-1;    
        int index = 0;
          // high == low,说明只有一个元素
        return quick(nums, 0, high, nums.size()/2);
    }
    int quick(vector<int>& nums, int low, int high, int middle){
        int index = partion(nums, low, high);
        if(index == middle){
            return nums[index];
        }else if(index > middle){
            return quick(nums, low, index-1, middle);
        }else{
            return quick(nums, index+1, high, middle);
        }
        return nums[index];
    }

    int partion(vector<int>& nums, int low, int high) {
        int i = low;
        int j = high+1;
        int pivot = nums[low];
        while (true) {
            while (i < high && nums[++i] < pivot) {
            }
            while (j > low && nums[--j] > pivot) {
            }
            if(i >= j){
                break;
            }
           swap(nums[i], nums[j]);
        }
        swap(nums[low], nums[j]);
        return j;
    }

};
```

执行用时：20 ms, 在所有 C++ 提交中击败了97.11%的用户

内存消耗：18.3 MB, 在所有 C++ 提交中击败了95.23%的用户

#### 版本1、版本2、版本3对比

两个版本的差别在于partion函数的实现

## 题解

### 一种基于快速排序的实现

```c++
class Solution 
{
   public:
    int majorityElement(vector<int>& nums)
    {
        return quickSearch(nums,0,nums.size()-1,nums.size()/2);
    }
    int quickSearch(vector<int>&  a,int left,int right,int m)
    {
        int index = Partition(a,left,right);
        if(index==m)
        {
            return a[index];
        }
        else if(index>m)
        {
            return quickSearch(a,left,index-1,m);
        }
        else
        {
            return quickSearch(a,index+1,right,m);
        }
    }
 int Partition(vector<int>&  a,int left,int right)
    {
        int i=left;
        int j=right+1;
        int pivot=a[left];
        while(true)
        {
            while(i<right && a[++i]<pivot) {}
            while(j>0 && a[--j]>pivot)     {}
            if(i>=j)
            {
                break;
            }
            else
            {
                swap(a,i,j);
            }
        }
        swap(a,left,j);
        return j;
    }
    void swap(vector<int>&  a,int i,int j)
    {
        int temp=a[j];
        a[j]=a[i];
        a[i]=temp;
    }
};
```

