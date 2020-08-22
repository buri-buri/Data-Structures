def BubbleSort():
    n=len(a)
    for i in range(n):
        for j in range(n):
            if(a[i]<a[j]):
                a[i],a[j]=a[j],a[i]
if __name__=='__main__':
    a=[3,2,5,7,-3,1,8,6,9,12,4,16,25,11]
    BubbleSort()
    print(a)