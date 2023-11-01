#include<iostream>
using namespace std;
void merge(int a[],int lower,int middle,int upper)
{
    int i,j,k=lower;
    int p=middle-lower+1;
    int q=upper-middle;
    int leftSubArray[p],rightSubArray[q];
    for(i=0;i<p;i++)
    leftSubArray[i]=a[lower+i];
    for(j=0;j<q;j++)
    rightSubArray[j]=a[middle+1+j];
    i=j=0;

    while(i<p && j<q)
    {
        if(leftSubArray[i]<=rightSubArray[j])
        {
            a[k]=leftSubArray[i];
            i++;
        }
        else
        {
            a[k]=rightSubArray[j];
            j++;
        }
        k++;
    }
    while(i<p)
    {
        a[k]=leftSubArray[i];
        i++;
        k++;
    }
    while(j<q)
    {
        a[k]=rightSubArray[j];
        j++;
        k++;
    }

}
void mergesort(int a[],int low,int high)
{
    if(low<high)
    {
        int mid=(low+high)/2;
        mergesort(a,low,mid);
        mergesort(a,mid+1,high);
        merge(a,low,mid,high);
    }
}
void printarray(int a[],int n)
{
    for(int i=0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
}
int main()
{
    int n;
    cout<<"Enter number of elements: ";
    cin>>n;
    int i=0,a[n],x[n]={};
    while(i<n)
    {
        cout<<"Element "<<i+1<<": ";
        cin>>a[i];
        i++;
    }
    mergesort(a,0,n-1);
    cout<<"\nSorted Array: ";
    printarray(a,n);
}