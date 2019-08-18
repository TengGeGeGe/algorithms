'''
@Descripttion: sort algorithms for python
@version: 
@Author: wuteng@mail2.sysu.edu.cn
@Date: 2019-08-18 10:22:18
@LastEditors: wuteng@mail2.sysu.edu.cn
@LastEditTime: 2019-08-18 16:55:13
'''
import random
import sys


class SortAlgorithms():

    def __init__(self, length):
        self.sort_array = []
        self.max = 1000
        self.min = 0
        # 初始化带排序数组
        for i in range(length):
            self.sort_array.append(random.randint(self.min, self.max))

    def insertion_sort(self, sort_array):
        '''
        @name: 
        @msg: 插入排序
        @param {type} sort_dir:str
        @return: sorted_array
        '''
        arr = sort_array.copy()
        for j in range(1, len(arr)):
            insert_key = arr[j]
            i = j - 1
            while i >= 0 and arr[i] > insert_key:
                arr[i + 1] = arr[i]
                i -= 1
            arr[i + 1] = insert_key
        return arr
            
    def merge_sort(self, sort_array, p, r):
        '''
        @name: 
        @msg: 归并排序
        @param {type} 
        @return: sorted_array
        '''
        if p < r:
            q = (p + r) // 2
            self.merge_sort(sort_array, p, q)
            self.merge_sort(sort_array, q + 1, r)
            self.__merge(sort_array, p, q, r)
        return sort_array

    def __merge(self, arr, p, q, r):
        '''
        @name: 
        @msg: 
        @param {type} p:start, q:middle, r:end
        @return: 
        '''
        arr1 = arr[p:q + 1]
        arr2 = arr[q + 1:r + 1]
        index1 = 0
        index2 = 0
        for i in range(p, r + 1): 
            value1 = arr1[index1] if index1 < len(arr1) else self.max + 1
            value2 = arr2[index2] if index2 < len(arr2) else self.max + 1
            if value1 > value2:
                arr[i] = value2
                index2 += 1
            else:
                arr[i] = value1
                index1 += 1

    
if __name__ == '__main__':
    array_length = 10
    sorter = SortAlgorithms(array_length)
    sort_array = sorter.sort_array
    # sorted_array = sorter.insertion_sort(sort_array)
    sorted_array = sorter.merge_sort(
        sort_array.copy(),
        0,
        array_length - 1)
    print('Before sort:', sort_array)
    print('After sort:', sorted_array)
