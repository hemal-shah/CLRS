#include<iostream>
#include<vector>

std::vector<int> A;
void write_vector(std::vector<int> v);
void merge_sort(int start, int end);
void merge(int start, int middle, int end);

int main(int argc, char const *argv[]) {

  int n;
  std::cout << "How many elements you want to insert?" << '\n';
  std::cin >> n;

  for (int i = 0; i < n; i++) {
    int temp;
    std::cin >> temp;
    A.push_back(temp);
  }

  std::cout << "Your input is : " << '\n';
  write_vector(A);

  merge_sort(0, n - 1);

  std::cout << "The sorted vector is : " << '\n';
  write_vector(A);
  return 0;
}


void write_vector(std::vector<int> v) {
  std::vector<int>::iterator itr = v.begin();
  while(itr != v.end()){
    std::cout << *itr << ' ';
    itr++;
  }
  std::cout << '\n';
}


void merge_sort(int start, int end){
  if (start < end){
    int middle = (start + end) / 2;
    merge_sort(start, middle);
    merge_sort(middle + 1, end);
    merge(start, middle, end);
  }
}


void merge(int start, int middle, int end){
  int num1 = middle - start + 1;
  int num2 = end - middle;
  std::vector<int> left, right;

  for (int i = 0; i < num1; i++) {
    left.push_back(A[i + start]);
  }

  for(int j = 0; j < num2; j++){
    right.push_back(A[middle + j + 1]);
  }

  int i = 0, j = 0, k = start;
  while (i < num1 && j < num2) {
    if(left[i] <= right[j]){
      A[k] = left[i];
      i++;
    } else{
      A[k] = right[j];
      j++;
    }
    k++;
  }

  while(i < num1){
    A[k] = left[i];
    i++;
    k++;
  }

  while(j < num2){
    A[k] = right[j];
    j++;
    k++;
  }
}
