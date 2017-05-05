#include<iostream>
int main(){
	int n;
	std::cout<<"Enter number of elements to sort: " ;
	std::cin>>n;
	int arr[n];
	for(int i = 0 ; i < n; i++){
		//taking inputs..
		std::cout<<"Enter element number "<<(i+1)<<" : ";
		std::cin>>arr[i];
	}

	for(int j = 1; j < n; j++){
		int key = arr[j];
		int i = j-1;
		while(i >= 0 && arr[i] < key){
			arr[i+1] = arr[i];
			i--;
		}
		arr[i+1] = key;
	}
	
	//printing the sorted sequence.
	for(int i = 0; i < n; i++)
		std::cout<<arr[i]<<" ";

	std::cout<<std::endl;
	return 0;
}