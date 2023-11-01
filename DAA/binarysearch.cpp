#include<iostream>
using namespace std;
int main(){
    int n,i,j,t;
    cout << "Enter size of array: ";
    cin>>n;
    int a[n];
    cout<<"Enter the elements of array:\n";
    for(i=0;i<n;i++)
    {
        cout<<"Element "<< i+1<<" =";
        cin>>a[i];
    }
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(a[j]>a[j+1])
            {
                t=a[j];
                a[j]=a[j+1];
                a[j+1]=t;
            }
        }
    }
    int target;
    cout<<"Enter target element: ";
    cin>>target;
    int start=0,end=n-1,mid,index;
    bool flag=true;
    while(flag)
    {
        mid=(start+end)/2;
        if(start>end)
        {
            cout<<"Target not found.";
            flag=false;
        }
        else if(a[mid]==target)
        {
            index=mid;
            cout<<"Target found at position "<<index+1;
            flag=false;
        }
        else if(a[mid]>target)
        {
            end=mid-1;
            continue;
        }
        else if(a[mid]<target)
        {
            start=mid+1;
            continue;
        }
    }
}