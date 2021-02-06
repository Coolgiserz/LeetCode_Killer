# 剑指Offer.56-2.数组中数字出现的次数2

##### 难度：中等

##### 关键词：位运算

##### 链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/

## 题目描述

在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

示例 1：

```
输入：nums = [3,4,3,3]
输出：4
```

示例 2：

```
输入：nums = [9,1,7,9,7,9,7]
输出：1
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

### 思路：二进制位的规律

出现了3次的数字的各个二进制位加和必然能被3整除。所以，如果将数组中所有数字的各个二进制位加和后对3取余，那个只出现过1次的数字的二进制位就昭然若揭了。

到目前为止，关键问题转变为：

1. 如何统计各个数字的二进制位并对3取余？
2. 如何从二进制位恢复到十进制的结果？

## 代码实现

```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        long bitMask = 1;
        int bitSum[32] = {0};
        int bitIndex = 0;
        //统计二进制位和
        for(int& num: nums){
            bitMask = 1;
            for(int j=31;j>=0;--j){
                int bit = num & bitMask;
                if(bit != 0){
                    bitSum[j] += 1;
                }
                bitMask = bitMask << 1;
            }
            
        }
        //除以3 //恢复
        for(int j=0;j<32;++j){
            result = result << 1;
            bitSum[j] = bitSum[j] % 3;
            result += bitSum[j];
            
        }

        return result;
    }
};
```

执行用时：52 ms, 在所有 C++ 提交中击败了78.19%的用户

内存消耗：15.8 MB, 在所有 C++ 提交中击败了83.96%的用户

## 题解

### 大神简解

```c++
class Solution {
    public int singleNumber(int[] nums) {
        int a = 0;
        int b = 0;
        
        for(int num : nums) {
        	a = (a ^ num) & ~b;
        	b = (b ^ num) & ~a;
        }
        
        return a;
    }
}
```

