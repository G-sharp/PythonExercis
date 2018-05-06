#!/usr/bin/python
#-*- coding=utf-8 -*-
'''
file: permutaion.py
Created on Thu Feb  1 10:16:28 2018
@author: gsharp

此为递归法进行的全排列算法
算法思路:
       列表长度为n
    1.n=1 输出自身
    2.n>1 逐一除掉各个元素 将剩下序列递归全排列
    
'''
COUNT=0
def perm(n,begin,end):
    global COUNT
    if begin>=end:
        print n
        COUNT +=1
    else:
        i=begin
        for num in range(begin,end):
            n[num],n[i]=n[i],n[num]
            perm(n,begin+1,end)
            n[num],n[i]=n[i],n[num]
n=['a','b','c','d']
perm(n,0,len(n))
print COUNT

'''
    插入法非递归全排列
    原理是插入法，也就是在一个有n个元素的已有排列中，
    后加入的元素，依次在每一个位置插入，生成n+1个新的全排列。
'''
def getArrayInsertCharToStr(STR,CHAR):
  arr =[]
  s_len = len(STR)
  index =0
  while index <= s_len:
    #分割字符串
    arr.append(STR[:index]+CHAR+STR[index:s_len])
    index = index + 1
  return arr  
 
def getArrayInsertCharToArray(array,CHAR):
  index = 0
  re_array = []
  while index < len(array):
    re_array = re_array + getArrayInsertCharToStr(array[index],CHAR)
    index = index + 1
  return re_array       
 
def getPermutation(STR):
    
    resultArr = [STR[0]]
    for item in STR[1:]:
        resultArr = getArrayInsertCharToArray(resultArr,item)
    return   resultArr
 
 
print(getPermutation('abcd'))
"""
非递归字典排序法全排列
要求初始序列为最小序列 如：1234 而不可为 1342 
只能排列具有值的元组
设P是集合{1，2，……n-1，n}的一个全排列：P=P1P2……Pj-1PjPj+1……Pn（1≤P1，P2，……，Pn≤n-1）
1.从排列的右端开始，找出第一个比右边数字小的数字的序号j，即j=max{i|Pi<Pi+1,i>j}在Pj的右边的数字中，
找出所有比Pj大的数字中最小的数字Pk，即k=min{i|Pi>Pj，i>j}
2.交换Pi，Pk
3.再将排列右端的递减部分Pj+1Pj+2……Pn倒转，因为j右端的数字是降序，所以只需要其左边和右边的交换，直到中间，因此可以得到一个新的排列P’=P1P2……Pj-1PkPn……Pj+2Pj+1
"""
def Swap(n,a,b):
    n[a],n[b] = n[b],n[a]
    return None
def Reverse(n,begin):
    if len(n) > begin:
        i = begin
        j = len(n)-1
        while i < j:
            Swap(n,i,j)
            i += 1
            j -= 1
    return n

def FindMin(n,i):
    j = len(n)-1
    k = i + 1
    while j > i:
        if n[j] > n[i] and n[j] < n[k]:
            k = j
        j -= 1
    return k

def Permut(n):
    count = 0
    j = len(n) -1  
    if j < 1:
        return n
    else :
        print n
        count += 1
        while j >= 1:
            i = j - 1
            if n[i] < n [j] :
                k = FindMin(n,i)
                Swap (n,i,k)
                Reverse (n,j)
                j = len(n) - 1
                count += 1
                print n
            else :
                j -= 1
    print count

n =[1,2,3,4]
Permut(n)
