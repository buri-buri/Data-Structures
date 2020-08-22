def MergeSort(a,l,r):
    if(r-l):
        mid=(l+r)//2
        MergeSort(a,l,mid)
        MergeSort(a,mid+1,r)
        merge(a,l,mid,r)

def merge(a,l,mid,r):
    left=a[l:mid+1]
    right=a[mid+1:r+1]
    k=l
    i=j=0
    while(l+i<=mid and mid+j+1<=r):
        if(left[i]<=right[j]):
            a[k]=left[i]
            i=i+1
        else:
            a[k]=right[j]
            j=j+1
        k=k+1
    if(l+i<=mid):
        while(k<=r):
            a[k]=left[i]
            i=i+1
            k=k+1
    else:
        while(k<=r):
            a[k]=right[j]
            j=j+1
            k=k+1

if __name__ == "__main__":
    a=[3,2,5,7,-3,1,8,6,9,12,4,16,25,11]
    MergeSort(a,0,len(a)-1)
    print(a)

'''
Algorithmic Paradigm: Divide and Conquer
T(n) = 2T(n/2) + Theta(n)
Complexity in all cases: O(NlogN)
Auxiliary Space: O(n)
Sorting In Place: No
Stable: Yes
'''
