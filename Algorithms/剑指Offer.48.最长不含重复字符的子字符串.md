# 剑指Offer.48.最长不含重复字符的子字符串

##### 难度：中等

##### 关键词：哈希表、双指针、滑动窗口

##### 链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/

## 题目描述

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:

```
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

示例 2:

```
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

示例 3:

```
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```


提示：

- s.length <= 40000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路1： 动态规划：哈希表+线性遍历

用一个哈希表记录每个字符上一次出现时的索引。遍历字符串中的每一个字符，计算其与上一次出现时的距离，如当前遍历字符为第i个字符，上一次出现时索引为prevIndex，则距离为$d=i-prevIndex$。记$f(i)$为以第i个字符为结尾的最长不重复子字符串长度，则$f(i-1)$和$d$的大小关系决定了$f(i)$。

时间复杂度O(N),空间复杂度O(K)，K为唯一字符个数。

### 思路2: 时间换空间

可否不引入哈希表解决该问题？

当然可以，哈希表的作用在于记录上一次出现的位置，从而计算出两个重复出现的字符之间的距离，没有哈希表则可以引入一个循环来计算这个距离。

## 代码实现

### 实现1: 数组代替哈希表

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.length()==0){
            return 0;
        }
        int MAX_COUNT = 256;
        int hashtable[MAX_COUNT];
        for(int i=0;i<MAX_COUNT;++i){
            hashtable[i] = -1;
        }

        int d = 0;
        int result = 0;
        for(int i=0;i<s.length();++i){
            int prevIndex = hashtable[s[i]-' '];
            
            if(prevIndex==-1 || i-prevIndex>d){
               //第i个字符上次出现的位置在以第i-1个字符为结尾的子字符串之前；
                ++d;

            }else{
                //第i个字符上次出现的位置在以第i-1个字符为结尾的子字符串中；
           
                d = i-prevIndex;
            }
            hashtable[s[i]-' '] = i;
            if(d>result){
                result = d;
            }
        }
        if(d>result){
             result = d;
        }
        return result;
    }
};
```

执行用时：8 ms, 在所有 C++ 提交中击败了89.57%的用户

内存消耗：6.8 MB, 在所有 C++ 提交中击败了97.72%的用户

### 实现2: 哈希表解法

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.length()==0){
            return 0;
        }
        unordered_map<char, int> _map;
  
        int d = 0;
        int result = 0;
        for(int i=0;i<s.length();++i){
            int  prevIndex = -1;
            if(_map.find(s[i])!=_map.end()){
                prevIndex =_map[s[i]];
            }
            
            
            if(prevIndex==-1 || i-prevIndex>d){
               //第i个字符上次出现的位置在以第i-1个字符为结尾的子字符串之前；
                ++d;

            }else{
                //第i个字符上次出现的位置在以第i-1个字符为结尾的子字符串中；
                
                d = i-prevIndex;
            }
            _map[s[i]] = i;
            if(d>result){
                result = d;
            }
        }
        if(d>result){
             result = d;
        }
        return result;
    }
};
```

执行用时：12 ms, 在所有 C++ 提交中击败了77.50%的用户

内存消耗：8.1 MB, 在所有 C++ 提交中击败了64.45%的用户

## 小结

该题目没有标明字符的边界，不能肯定只有26个字母，应考虑更宽广的范围，如是不是涵盖整个ascii码表？还是有更广的范围？

如果字符范围很广且无规律，则不能简单地用数组代替哈希表。