#include <bits/stdc++.h>
using namespace std;
int  main()
{
   for(int i=1000;i<=9999;i++)
   {
       int tot=0; 
       for(int j=1;j<i;j++)
       {
           if(i%j==0)
           {
               tot+=j;
           }
       }
       if(i==tot) cout<<i<<endl; 
   }
   for(int i=100;i<=999;i++)
   {
       int sum=0; 
       int temp=i; 
       while(temp)
       {
           int digit=temp%10; 
           temp/=10; 
           sum+=digit*digit*digit; 
       }
       if(sum==i) cout<<sum<<' '; 
   }
}
