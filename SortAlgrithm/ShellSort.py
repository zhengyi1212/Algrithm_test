#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-22 下午3:42
# @Author  : zhuzhengyi
# @File    : ShellSort.py
# @Software: PyCharm
'''
1959年Shell发明，第一个突破O(n2)的排序算法，是简单插入排序的改进版。
它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。
与简单插入排序相比，减少了移位操作

算法描述
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：

选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
按增量序列个数k，对序列进行k 趟排序；
每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
'''

def shellsort(array):
	gap = len(array)//2     #将数组分成gap个组，且每个组中，元素间的距离为gap
	while gap>0:
		for i in range(gap,len(array)):
			tmp = array[i]
			j = i-gap
			while j>=0 and tmp < array[j]:
				array[j+gap]=array[j]
				j -= gap
			array[j+gap]=tmp
		gap //=2

	pass

nums = [6,1,2,7,9,3,4,5,10,8]
print('\ninit data:',nums)
shellsort(nums)
print('sorted:',nums)