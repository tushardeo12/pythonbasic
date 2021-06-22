#include <stdio.h>
int main()
{
	const int max = 100;
	int arr[max];
	int i, n, x, flag;
	printf("Enter the length");
	scanf("%d", &n);
	printf("Enter the elements in array");
	for (i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
	}
	printf("Enter the value which we are searching");
	scanf("%d", &x);
	flag = 0;
	for (i = 0; i < n; i++)
	{
		if (arr[i] == x)
		{
			flag = 1;
			break;
		}
	}
	if (flag == 1)
	{
		printf("%d is found", &x);
	}
	else
	{
		printf("%d is not found", &x);
	}
	return 0;
}
