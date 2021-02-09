# 剑指Offer.59-1.滑动窗口的最大值

##### 难度：简单

##### 关键词：队列、滑动窗口

##### 链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/

## 题目描述

给定一个数组 `nums` 和滑动窗口的大小 `k`，请找出所有滑动窗口里的最大值。

示例:

```
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值

---------------               -----

[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

提示：

- 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

之前实现过[剑指Offer.30.包含min函数的栈](剑指Offer.30.包含min函数的栈.md)，其本质上是通过辅助栈保证在push、pop元素之后都能以O(1)时间复杂度访问到栈中元素。这里的条件也类似，滑动窗口的每一次窗口滑动可以看作是同时发生了push和pop，因此也可以沿用先前的经验，添加一个辅助容器来记录每个滑动窗口的最大值（索引）。

遍历nums数组的过程中，将有可能成为滑动窗口最大值的元素添加到辅助队列中，当辅助队列中的值不可能成为滑动窗口最大值的时候（如超过了滑动窗口的范围），将其移出。

## 代码实现

```c++
class Solution {
public:

    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        
        vector<int> result;
        if(nums.size()==0){
            return result;
        }
        if(nums.size()>=k && k>=1){
            deque<int> _deque;
            for(int i=0;i<nums.size();++i){
                if(i>k-1){
                    result.push_back(nums[_deque.front()]);
                  	//滑动窗口已经后移，将队列中不可能成为滑动窗口最大值的元素——与当前位置的差在k以上的位置——去掉
                    if(!_deque.empty() && (i - _deque.front()) >= k){
                        _deque.pop_front();
                    }

                }
               //第i位置的元素如果大于队列尾元素，则将队列尾元素移出，因尾元素已经不可能成为i所在滑动窗口的最大值
                while(!_deque.empty() && nums[_deque.back()] <= nums[i]){
                    _deque.pop_back();   
                }
                _deque.push_back(i);
            }
            result.emplace_back(nums[_deque.front()]);
        }

        return result;

    }
};
```

执行用时：16 ms, 在所有 C++ 提交中击败了99.01%的用户

内存消耗：15.4 MB, 在所有 C++ 提交中击败了87.84%的用户

## 题解

