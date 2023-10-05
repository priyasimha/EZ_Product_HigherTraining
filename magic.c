#include<stdio.h>
void main()
{
	int n=3,i,j,c;
	int ke=0,ko=0;
	int even[n+1],odd[n+1],arr[n][n];
	//input
	for(i=1;i<=n*n;i++)
	{
		if(i%2==0)
		{
			even[ke]=i;
			ke++;
		}else{
			odd[ko]=i;
			ko++;
		}
	}
	//logic
	ke=0;
	ko--;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
		{
			if(i==n-1 && j==n-1)
			{
				arr[i-1][j-1]=odd[ko];
				ko--;
			}else if((i+j)%2==0)
			{
				arr[i-1][j-1]=even[ke];
				ke++;
			}else{
				arr[i-1][j-1]=odd[ko];
				ko--;
			}
		}
	}
	//print original
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("%d ",arr[i][j]);
		}
		printf("\n");
	}

}