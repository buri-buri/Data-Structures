'''
EXPLANATION

A=[7,2,1,6,8,5,3,4]
yha bhi isme hum partition krte hai list ka
first select a PIVOT element then arrange that pivot element in such a way that all the element smaller than pivot are before it and all the elments greater than pivot are ahead of it.
Pivot element = a[-1] = 4
now after rearranging
a=[2,1,3,'4',8,5,7,6] ye 4 se pehle ab ek list hai and 4 kai baad ek list and 4 element jo hai vo apni sahi place pe hai.
now we have 2 SubProblems --> [2,1,3] and [8,5,7,6]
Now again do this procedure (partitioning logic) for both of these array's.2

a=[2,1,3]
pivot = a[-1] = 3
Now rearrange, after rearrange 3 apni jagah par hi hai to simple isme keval 1 sub problem create hogi --> [2,1]

a=[2,1]
pivot = 1
after rearrange, a=[1,2] , now subproblem --> [2]
# when length = 1 hum partitioning nhi krege bcoz length array sorted hi hota hai.


a=[8,5,7,6]
pivot = a[-1] = 6
rearrange = [5,6,7,8]
now again make call for sub problems --> Partition()
Partition() function element set krta jaa rha hai.
'''

# Understanding Partitioning Logic
'''
a=[7,2,1,6,8,5,3,4]
pivot = 4; l=0; r=7
index=0, index hi MID hai, cuurently index=0 hai , but use MID bnana hai ,kesehume bss pivot se chote elements ko MIDindex se pehle laana hai
cuurently, index = l = 0 hai and pivot=4 hai
loop lgaa (l,r) tak ka and jo bhi element pivot se chota hoga use index se pehle bhej dege mtlb 
let currently index = xyz hai and loop mai  i=112 hai and element at a[112]=1 and pivot=4 hai
to pivot>a[112] to uss element ko index se pehle vaale indexes mai bhejna hai taaki hum keh ske ki INDEX se pehle jitne bhi indexes hai unme PIVOT se choote elements hai to at the end of loop index se pehle jitne bhi indexes hoge (0 to index-1) unme elements PIVOT se choote hoge

def partition():
    pivot=a[r]   #pivot = a[-1] if a=a[l:r] , but yha mai poora arr le rha hu, auxillary space nhi le rha
    index=l
    for i in range(l,r):
        if(a[i]<=pivot):
            swap(a[i],a[index])
            index+=1
at i=0 a[i]=7 , pivot = 4 if(condition) -> false. arr=[7,2,1,6,8,5,3,4] # No_Change
at i=1 a[i]=2 , pivot > 2, to swap(a[i],a[index])  --> swap(a[1],a[0])  --> the increment index += 1 now arr=[2,7,1,6,8,5,3,4]
at i=2 a[i]=1 , pivot > 1, swap(a[i],a[index]) --> swap(a[2],a[1]) --> arr=[2,1,7,6,8,5,3,4]
at i=3,4,5, if(condition) --> False.

Now i=6 index=2 hai abhi tak
at i=6 , a[i]=3, pivot>3 to swap(a[i],a[2])
Loop Ends
AFTER LOOP,
a=[2,1,3,6,8,5,7,4]
index=3 hai
but isse abhi pivot apni position pe set nhi hua hai isley after loop
swap(a[index],pivot)
'''
def partition(a,l,r):
    pivot=a[r]
    index=l
    for i in range(l,r):
        if(a[i]<=pivot):
            a[i],a[index]=a[index],a[i]
            index+=1
    a[index],a[r]=a[r],a[index]
    return index
def QuickSort(a,l,r):
    if(l<r):
        mid=partition(a,l,r) 
        QuickSort(a,l,mid-1)
        QuickSort(a,mid+1,r)
    
if __name__ == "__main__":
    a=[3,2,5,7,-3,1,8,6,9,12,4,16,25,11]
    QuickSort(a,0,len(a)-1)
    print(a)


'''
Algorithmic Paradigm: Divide and Conquer
Best Case = Average Case = O(NlogN)
Worst Case:O(N*N)
Auxiliary Space: O(n)
Sorting In Place: Yes
Stable Sort: No
'''
