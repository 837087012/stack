#链表成栈
from typing import Any,List,Optional
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return 'Node(%s)'%(self.data)
class Stack:
    def __init__(self):
        self.top=None
        self.size=0
    def push(self,data):
        node=Node(data)
        node.next=self.top
        self.top=node
        self.size+=1
    def pop(self):
        if self.top is None:
            raise Exception ('空栈')
        elif self.top.next:
            temp=self.top
            self.top=self.top.next
            self.size-=1
        else:
            temp=self.top
            self.size-=1
        return temp
    def is_empty(self):
        return not bool(self.top)
    def print_link(self):
        curr=self.top
        string_stc=''
        while curr:
            string_stc+='%s->'%(curr)
            curr=curr.next
        return string_stc+'end'
    def size(self):
        return self.size
class Stack_1ist:
    def __init__(self,limit=10):
        self.stack=[]
        self.size=0
    def __str__(self):
        return  str('%s')%(self.stack)
    def push(self,data):
        self.stack.append(data)
        self.size+=1
    def pop(self):
        if self.stack:
            temp=self.stack.pop()
            self.size -= 1
        return temp

    def peek(self):
        if self.stack:
            return self.stack[-1]
    def is_empty(self):
        return not bool(self.stack)
    def size(self):
        return self.size
class Solution:
    def remove1(self,nums,target):  #去目标变量，返回不重复的值
        fast=0
        slow=0
        while fast<len(nums):
            if nums[fast]==target:
                fast+=1
            else:
                nums[slow]=nums[fast]
                slow+=1
                fast+=1
        return slow,nums[:slow]
    def remove2(self,nums):  #零后移
        fast=0
        slow=0
        while fast<len(nums):
            if nums[fast]==0:
                fast+=1
            else:
                nums[slow]=nums[fast]
                slow+=1
                fast+=1
        for i in range(slow,len(nums)):
            nums[i]=0
        return nums
    def remove(self,nums,target):  #之和，有序列表
        right=len(nums)-1
        left=0
        while left<right:
            curr=nums[left]+nums[right]
            if curr==target:
                return left,right
                left+=1
                right-=1
            else:
                if curr<target:
                    left+=1
                else:
                    right+=1
    def dic(self,nums,target):
        dic={}
        for i in range(len(nums)):
            j=target-nums[i]
            if j in dic:
                return dic[j],i
            else:
                dic[nums[i]]=i
    def remove3(self,nums):   #去重复值,返回不重复列表长度
        fast=0
        slow=0
        while fast<len(nums):
            if nums[fast]==nums[slow]:
                fast+=1
            else:
                slow += 1
                nums[slow]=nums[fast]

                fast+=1
        return slow+1,nums[:slow+1]

if __name__ == '__main__':
    stack=Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.size)
    print(stack.print_link())
    print(stack.pop())
    print(stack.print_link())
    print(stack.is_empty())
    print(stack.size)
    # stack_1=Stack_1ist()
    # print(stack_1.is_empty())
    # for i in range(10):
    #     stack_1.push(i)
    # print(stack_1)
    # for j in range(5):
    #     stack_1.pop()
    # print(stack_1)
    # print(stack_1.peek())
    # print(stack_1.size)
    # print(stack_1.is_empty())
    # solu=Solution()
    # print(solu.remove([1,2,3,4,1,1,2,3],6))
    # print(solu.dic([1,2,3,4,1,1,2,3],6))
    # print(solu.remove1([1,2,3,4,1,3],1))
    # print(solu.remove2([0,1,2,30,0,1]))
    # print(solu.remove3([1,1,2,2]))