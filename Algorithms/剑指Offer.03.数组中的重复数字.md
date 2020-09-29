

# 剑指Offer.03.数组中的重复数字

##### 难度：简单

##### 关键词：数组、哈希表

##### 链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/

## 题目描述

找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

```
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
```

**限制：**

```
2 <= n <= 100000
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

## 代码实现

### 实现1：哈希表计数

```c++
class Solution {
public:
    //思路1. 1）哈希表计数 2）返回计数为1的结果
    //思路2. 1）进行排序 2）检查排序后数组与下标是否有矛盾

    // 思路1
    int findRepeatNumber(vector<int>& nums) {
        unordered_map<int, int> _map;
        for(int &num: nums){
            if(_map.find(num) != _map.end()){
                _map[num]++;
            }else{
                _map[num] = 1;
            }
        }
        for(auto iter=_map.begin(); iter!=_map.end(); ++iter){
            if(iter->second > 1){
                return iter->first;
            }
        }
        return -1;
    }
};
```

执行用时：184 ms, 在所有 C++ 提交中击败了8.74%的用户

内存消耗：35.2 MB, 在所有 C++ 提交中击败了5.03%的用户

### 实现2:

实现1明显很低效，使用了笨重的unordered_map。实际上由于题目的特殊性：长度为n的数组内的数字都在0～n-1范围内，所以可以采用数组替代哈希表，数组下标作为哈希表的key。实现空间优化

```c++
class Solution {
public:
    //思路1. 1）哈希表计数 2）返回计数为1的结果
    //思路2. 1）进行排序 2）检查排序后数组与下标是否有矛盾

    // 思路1.1
    int findRepeatNumber(vector<int>& nums) {
        vector<int> _map(nums.size());
        int i = 0;
        for(int &num: nums){
            _map[num]++;
            ++i;
         
        }
        i = 0;
        for(i=0;i<_map.size();i++){
            if(_map[i] > 1){
                return i;
            }
        }
        return -1;
    }
};
```

执行用时：88 ms, 在所有 C++ 提交中击败了78.11%的用户

内存消耗：23.3 MB, 在所有 C++ 提交中击败了38.99%的用户

### 实现3:

先排序，后找矛盾。时间换空间：

```c++
class Solution {
public:
    //思路1. 1）哈希表计数 2）返回计数为1的结果
    //思路2. 1）进行排序 2）检查排序后数组与下标是否有矛盾

    // 思路2
    int findRepeatNumber(vector<int>& nums) {
        if(nums.size() == 0){
            return -1;
        }
        int tmp = nums[0];//n一定大于等于2
        int res = -1;
        std::sort(nums.begin(), nums.end());
        
        for(int i=1;i<nums.size();i++){
            if(nums[i]==tmp){
                res = nums[i];
                return res;
            }else{
                tmp = nums[i];
            }
        }
        return res;
    }
};
```

执行用时：136 ms, 在所有 C++ 提交中击败了30.92%的用户

内存消耗：22.6 MB, 在所有 C++ 提交中击败了56.67%的用户

## 小结

### 关于unordered_map的一些笔记

C++中的哈希表实现

如果要查看某个元素是否在表中，可通过find()方法

```c++
iterator find( const Key& key );
const_iterator find( const Key& key ) const;
```

若map.find(element) != map.end()，则说明表中存在元素。详见https://en.cppreference.com/w/cpp/container/unordered_map/find

C++20引入了新方法contains，可直接返回布尔类型，使用起来更加自然。（但Leetcode编译器目前貌似还不支持C++20）

```c++
bool contains( const Key& key ) const;
```

详见https://en.cppreference.com/w/cpp/container/unordered_map/contains

### 关于int[]和std::array、std::vector的对比

（考虑变长或定长、数据访问的灵活性、内存地址的连续性、并发访问的安全性、……）

Int[]指定数组大小时，所指定的大小必须是大于0的整型常量。

std::vector是动态数组，可以不固定大小

std::array也是定长容器

参考：https://blog.csdn.net/acelit/article/details/68068207

### ++i和i++的对比

暂略

## 报错

#### 问题1

```c++
class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        int tmp = nums[0];//n一定大于等于2
        int res = -1;
        std::sort(nums.begin(), nums.end());
        
        for(int i=1;i<nums.size();i++){
            if(nums[i]==tmp){
                res = nums[i];
            }else{
                tmp = nums[i];
            }
        }
        return res;
    }
};
```

如上代码产生了如下错误

```
/usr/bin/../lib/gcc/x86_64-linux-gnu/8/../../../../include/c++/8/bits/stl_vector.h:933:9: runtime error: reference binding to null pointer of type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior /usr/bin/../lib/gcc/x86_64-linux-gnu/8/../../../../include/c++/8/bits/stl_vector.h:933:9 in 
prog_joined.cpp:18:19: runtime error: load of null pointer of type '__gnu_cxx::__alloc_traits<std::allocator<int>, int>::value_type' (aka 'int')
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior prog_joined.cpp:18:19 in 

Program got signal SIGSEGV.
```

可能原因分析：

数组越界。

具体场景来看，可能是**对空数组的测试用例没处理好**；也可能是对非空数组的测试用例没处理好。