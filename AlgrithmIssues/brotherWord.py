#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-8-26 下午8:24
# @Author  : zhuzhengyi
# @File    : brotherWord.py
# @Software: PyCharm

'''
给你一个单词a，如果通过交换单词中字母的顺序可以得到另外的单词b，那么定义b是a的兄弟单词。
现在给你一个字典，用户输入一个单词，让你根据字典找出这个单词有多少个兄弟单词。

提示：将每个的单词按照字母排序，则兄弟单词拥有一致的字母排序（作为单词签名）。使用单词签名来查找兄弟单词。
实现过程：将用户给定的单词排好序，另存为standard，
遍历一遍字典，对每个单词排好序之后，如果与standard相同，则为兄弟单词
'''
