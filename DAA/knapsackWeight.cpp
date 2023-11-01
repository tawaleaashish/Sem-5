#include<iostream>
using namespace std;
int main(){
    int weight[]={20, 10, 30};
    int profit[]={100, 60, 120};
    int max_weight=50;
    int n=sizeof(weight)/sizeof(weight[0]);
    int i,j,t;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(weight[j]>weight[j+1])
            {
                t=profit[j];
                profit[j]=profit[j+1];
                profit[j+1]=t;

                t=weight[j];
                weight[j]=weight[j+1];
                weight[j+1]=t;
            }
        }
    }
    double max_profit=0.0;
    for(i=0;i<n;i++)
    {
        if(weight[i]<max_weight)
        {
            max_profit+=profit[i];
            max_weight-=weight[i];
        }
        else
        {
            max_profit+=profit[i]*((double)max_weight/(double)weight[i]);
            break;
        }
    }
    cout<<"Maximun Profit achieved is: "<<max_profit;
}