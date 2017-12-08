#-*- coding: utf-8 -*-


'''
Insert Sort （插入排序）:
输入： n 个数的1个序列 <a1,a2,a3,a4,...,an>
输出： 满足 a1<=a2<=a3<=...<=an 的序列
'''

class InsertSort:

    @staticmethod
    def InsertOrderSort(list):
        for index in range(1, len(list)):
            key = list[index]
            preIndex = index - 1
            while preIndex >= 0 and list[preIndex] > key:
                list[preIndex+1] = list[preIndex]
                preIndex -= 1
            list[preIndex + 1] = key
        print(list)

InsertSort.InsertOrderSort([1,3,2,4,5,56])
