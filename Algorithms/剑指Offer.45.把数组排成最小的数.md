# 剑指Offer.45.把数组排成最小的数

##### 难度：中等

##### 关键词：数学、排序

##### 链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/

## 题目描述

输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:

```
输入: [10,2]
输出: "102"
```

示例 2:

```
输入: [3,30,34,5,9]
输出: "3033459"
```


提示:

- 0 < nums.length <= 100

说明:

- 输出结果可能非常大，所以你需要返回一个字符串而不是整数
- 拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

原问题可以转换成一个对数组进行自定义排序的问题，关键在于实现新的排序规则。

## 代码实现

```c++
class Solution {
public:

    string minNumber(vector<int>& nums) {
        string result = "";
        int length = nums.size();
        vector<string> strNums(length);//将原来的数字存储为字符串
        for(int i=0;i<length;++i){
            strNums[i]= to_string(nums[i]);
        }
        sort(strNums.begin(), strNums.end(),  compare);

        for(int i=0;i<strNums.size();++i){
            result += strNums[i];
        }

        return result;
    }
private:
    static bool compare(string& s1, string& s2){
        return s1+s2<s2+s1;
    }

};
```

执行用时：8 ms, 在所有 C++ 提交中击败了89.08%的用户

内存消耗：10.9 MB, 在所有 C++ 提交中击败了95.72%的用户

## 题解

