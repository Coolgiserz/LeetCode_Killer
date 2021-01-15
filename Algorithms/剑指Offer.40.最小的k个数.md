# 剑指Offer.40.最小的k个数

##### 难度：简单

##### 关键词：堆、分治算法

##### 链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

## 题目描述

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：

```
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
```

示例 2：

```
输入：arr = [0,1,2,1], k = 1
输出：[0]
```

**限制：**

- `0 <= k <= arr.length <= 10000`
- `0 <= arr[i] <= 10000`

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

引入一个大小为k的辅助容器用于存储arr中最小的k个数。遍历一遍arr数组，当辅助容器存储元素个数小于k时，则将元素推入容器，否则取出容器中最大的元素与当前遍历元素比较，若当前遍历元素更小则将其替换掉容器中最大的元素（更新容器），直到遍历完arr。

可以使用最大堆或者multiset数据结构作为辅助容器。

## 代码实现

### 实现1: 基于优先队列辅助

```c++
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        if(k<1 || k>arr.size()){
            return vector<int>();
        }
				priority_queue<int> _queue;
        vector<int> output;
      	for(int& num: arr){
          	if(_queue.size()<k){
              	_queue.push(num);
            }else{
               int top = _queue.top();
              if(num < top){
                _queue.pop();
                _queue.push(num);
              }
               
            }
        }
      while(!_queue.empty()){
        int n = _queue.top();
        _queue.pop();
        output.emplace_back(n);
      }
      return output;
    }
};
```

执行用时：36 ms, 在所有 C++ 提交中击败了99.73%的用户

内存消耗：19.4 MB, 在所有 C++ 提交中击败了30.79%的用户

遍历元素arr需要O(n)时间复杂度，对于每个元素取出辅助容器中最大值或者更新辅助容器的元素平均需要logk复杂度，总共O(nlogk)时间复杂度

## 题解

- [最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/zui-xiao-de-kge-shu-by-leetcode-solution/)

## 知识点

### multiset

http://www.cplusplus.com/reference/set/multiset/

multiset是按照特定顺序存储元素的容器，多个元素可以具有等值。

在multiset中，一个元素的值也是它的标识（值本身就是键，类型为T）。multiset中元素的值在容器中不能被修改一次（元素总是const），但它们可以从容器中插入或删除。

在内部，multiset中的元素总是按照其内部比较对象（类型为Compare）所指示的特定严格的弱排序标准进行排序。

multiset容器通过键访问单个元素的速度通常比unordered_multiset集容器慢，但它们允许根据子集的顺序直接迭代。

multiset通常以二叉搜索树的形式实现。

