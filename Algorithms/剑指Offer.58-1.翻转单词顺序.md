# 剑指Offer.58-1.翻转单词顺序

##### 难度：简单

##### 关键词：字符串

##### 链接：https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/

## 题目描述

输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

 **示例 1：**

```
输入: "the sky is blue"
输出: "blue is sky the"
```

示例 2：

```
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
```

示例 3：

```
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
```

说明：

- 无空格字符构成一个单词。
- 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
- 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

注意：本题与主站 151 题相同：https://leetcode-cn.com/problems/reverse-words-in-a-string/

注意：此题对比原题有改动

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路

可以先把整个字符串翻转，然后将每个单词的字符翻转。

所以问题转变成：

1. 如何将整个字符串翻转？
2. 如何将每个单词翻转？
   - 如何判断一个单词的起始和结束？
   - 如何翻转？

## 代码实现

```c++
class Solution {
public:
    string reverseWords(string s) {
        
        string blanks("\f\v\r\t\n ");
        s.erase(0,s.find_first_not_of(blanks));
        s.erase(s.find_last_not_of(blanks) + 1);
        if(s.length()==0){
            return "";
        }
        //翻转
        reverseString(s, 0, s.length()-1);        
        string result;
        reverseWord(s, result);
        checkString(result);
        return result;
    }

    void reverseWord(string s, string& result){
        //
        int ind = 0;
        int start = 0;
        while(ind <= s.length()){
            if( (ind == s.length()) || (s[ind] == ' ')){
                reverseString(s, start, --ind);
                ++ind;
                start = ++ind;
            }else{
                ++ind;
            }
        }
        result = s;
        return;
    }

    void checkString(string& s){
        
        int i = 0;
        while(i<s.length()-1){
            while(s[i] == ' ' && s[i] == s[i+1]){
                s.erase(i,1);
            }
            ++i;
        }
        
    }

    //翻转字符串
    void reverseString(string& s, int start, int end){
        while(start<end){
            char tmp = s[start];
            s[start] = s[end];
            s[end] = tmp;
            ++start;
            --end;
        }
        return;
    }
};
```

执行用时：4 ms, 在所有 C++ 提交中击败了90.93%的用户

内存消耗：7.5 MB, 在所有 C++ 提交中击败了89.66%的用户

## 题解

