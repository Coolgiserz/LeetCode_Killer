# 剑指Offer.41.数据流中的中位数

##### 难度：困难

##### 关键词：设计、堆

##### 链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/

## 题目描述

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

- void addNum(int num) - 从数据流中添加一个整数到数据结构中。
- double findMedian() - 返回目前所有元素的中位数。

示例 1：

```
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
```

示例 2：

```
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]


```

限制：

- 最多会对 addNum、findMedian 进行 50000 次调用。

  注意：本题与主站 295 题相同：https://leetcode-cn.com/problems/find-median-from-data-stream/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 题目解析

可以考虑用数组、有序链表、二叉搜索树等数据结构。

其中数组最为简单，不要求排序的情况下插入元素的时间复杂度为O(1)，寻找中位数的复杂度为O(n)；

有序链表中插入元素的时间复杂度为O(n)，若以两个辅助指针指向有序链表中间的元素，则寻找中位数的复杂度为O(1)；

二叉搜索树如果是平衡的二叉树，则插入节点的复杂度为O(logN)，查找中位数的复杂度为O(1); 非平衡二叉树在最差的情况下会退化成有序链表，也不能以O(1)的复杂度查找中位数

综上，平衡二叉树是比较合适（效率高）的数据结构。

但实现平衡二叉树有些许困难，本题还可以用2个堆来达成O(1)查找中位数，O(k)插入元素的效果。

### 思路：最大堆+最小堆

考虑将数据流平均分配存放到两个堆中：一个最大堆一个最小堆，并保证最小堆的元素全部大于或等于最大堆的元素。如此则可以以O(1)的时间复杂度获取数据流的中位数，插入元素的复杂度也大大降低（不需要对所有元素进行排序，只需要对少数几个元素进行排序即可）

#### 测试用例

```
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
[[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]
```



## 代码实现

```c++
class MedianFinder {
public:
    vector<int> _min;//最小堆
    vector<int> _max;//最大堆
   
    /** initialize your data structure here. */
    MedianFinder() {
        
        make_heap(_min.begin(), _min.end(), greater<int>());
        make_heap(_max.begin(), _max.end(), less<int>());

    }
    
    //根据数据流中元素的奇偶性决定将新元素添加到哪个堆
    void addNum(int num) {
        int size = _max.size() + _min.size();
        if((size & 1) == 0){//偶数，添加到最小堆（不失一般性）
            if(size == 0){//容器为空
                _min.push_back(num);
            }else{
                int top = _max[0];
                if(num < top){
                    pop_heap(_max.begin(), _max.end());
                    _max.pop_back();

                    _max.push_back(num);
                    push_heap(_max.begin(), _max.end());
                    _min.push_back(top);
                }else{
                    _min.push_back(num);
                }
            }
            push_heap(_min.begin(), _min.end(), greater<int>()); // 小顶堆操作，需要附带第三个参数

        }else{//奇数；此时最小堆比最大堆多一个元素
            int top = _min[0];
            if(top > num){//放入最大堆
                 _max.push_back(num);
                 push_heap(_max.begin(), _max.end());
            }else{//top入最大堆，num如最小堆
                pop_heap(_min.begin(), _min.end(), greater<int>());
                _min.pop_back();

                _min.push_back(num);
                push_heap(_min.begin(), _min.end(), greater<int>());

                _max.push_back(top);
                push_heap(_max.begin(), _max.end());
            }
           
        }
    }
    
    double findMedian() {
        int size = _max.size() + _min.size();
        if((size&1) == 0){
            double maxV = _max[0];
            double minV = _min[0];
            return (maxV+minV)/2;

        }else{
            return _min[0];
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
```

执行用时：112 ms, 在所有 C++ 提交中击败了99.21%的用户

内存消耗：40.8 MB, 在所有 C++ 提交中击败了91.64%的用户

## 题解

