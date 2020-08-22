def InsertionSort(): 
    n=len(a)
    for i in range(1,n): 
        temp=a[i] 
        j = i-1
        while(j>=0 and a[j]>temp): 
            a[j+1]=a[j]
            j -= 1
        a[j+1]=temp
if __name__=='__main__':
    a=[3,2,5,7,-3,1,8,6,9,12,4,16,25,11]
    InsertionSort()
    print(a)

'''
Best Case : O(N)
Average Case = Worst Case = O(N*N)
'''