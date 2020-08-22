from heapq import (
    heapify,
    heappush as push,
    heappop as pop,
    heappushpop as pushpop)
def HeapSort():
    heap=[]
    sorted_arr=[]
    n=len(a)
    for i in range(n):
        push(heap,a[i])
    while(heap):
        sorted_arr.append(pop(heap))
    return sorted_arr
if __name__ == "__main__":
    a=[3,2,5,7,-3,1,8,6,9,12,4,16,25,11]
    a=HeapSort()
    print(a)

'''
Algorithmic Paradigm: Priority Queue
Best Case: O(N)
Average Case = Worst case = O(NlogN)
Auxiliary Space: O(n)
Sorting In Place: Yes
Stable Sort: No
'''