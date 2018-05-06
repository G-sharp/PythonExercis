#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
File: partition.py

Created on 1st Tue 16:59 2018

@author: Gsharp

以给定值x为基准将链表分割成两部分，所有小于x的结点排在大于或等于x的结点之前
给定一个链表的头指针 ListNode* pHead，请返回重新排列后的链表的头指针。
注意：分割以后保持原来的数据顺序不变。

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def partition(pHead,x):
    smallHead = ListNode(0)
    higHead = ListNode(0)
    small = smallHead
    big = bigHead
    while pHead is not None:
        if pHead.val < x:
       	    small.next = pHead
            small = small.next
        else:
            big.next = pHead
            big = big.next
        pHead = pHead.next
    big.next = None
    small.next = bigHead.next
    return smallHead.next
    
