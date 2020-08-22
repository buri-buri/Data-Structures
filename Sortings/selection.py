def give_min_value_index(ind,n):
    index=-1
    item=float('inf')
    for i in range(ind,n):
        if(item>a[i]):
            item=a[i]
            index=i
    return index
def SelectionSort():
    n=len(a)
    for i in range(n):
        ind=give_min_value_index(i,n)
        a[i],a[ind]=a[ind],a[i]
if __name__ == "__main__":
    a=[3,2,5,7,-3,1,8,6,9,12,4,16,25,11]
    SelectionSort()
    print(a)