int main()
{
int arr[] = {10,90,49,2,1,5,23};
int n= sizeof(arr)/sizeof(arr[0]);
sortInWave(arr,n);
for(int i=0; i<n; i++)
cout << arr[i] << " ";
return 0;
}
