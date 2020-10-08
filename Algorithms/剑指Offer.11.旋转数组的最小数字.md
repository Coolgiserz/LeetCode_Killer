# 剑指Offer.11.旋转数组的最小数字

##### 难度：简单

##### 关键词：二分查找

##### 链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

## 题目描述

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

```
输入：[3,4,5,1,2]
输出：1
```

示例 2：

```
输入：[2,2,2,0,1]
输出：0
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

## 代码实现

```c++
class Solution {
public:
    //测试用例：1）功能测试：无重复数字的数组、有重复数字的数组；2）特殊输入：空数组、旋转数为0

    //思路：二分法。如何利用上「递增排序」这一信息？二分排序；什么时候无法二分？中间元素无法帮助我们确定方向的时候。如何二分？
    int minArray(vector<int>& numbers) {
        if(numbers.size()==0){
            return -1;
        }
        int left = 0;
        int right = numbers.size()-1;
        int mid = left;

        while(numbers[left] >= numbers[right]){
            mid = (left+right)/2;
            // int midValue = (numbers[left]+numbers[right])/2;

            if(numbers[left] == numbers[right]  && numbers[right] == numbers[mid]){
                //无法二分
                return minArrayN(numbers);
            }
           
            if(numbers[mid]>=numbers[left]){//前数组较长
                left = mid;

            }else{
                right = mid;
            }
            if(right - left == 1){//结束循环
                return numbers[right];
            }
        }
        return numbers[mid];

    }

    int minArrayN(vector<int>& numbers){

        int res = numbers[0];
        for(int i=1;i<numbers.size();i++){
            if(res > numbers[i]){
                res = numbers[i];
            }
        }
        return res;
    }
};
```

执行用时：8 ms, 在所有 C++ 提交中击败了93.99%的用户

内存消耗：11.8 MB, 在所有 C++ 提交中击败了66.97%的用户

## 问题

### ==号不能连续用？

```c++
        if(numbers[left] == numbers[right] == numbers[mid]){
            //无法二分
            return minArrayN(numbers);
        }
```


```c++
        if(numbers[left] == numbers[right]  && numbers[right] == numbers[mid]){
            //无法二分
            return minArrayN(numbers)
        }
```





