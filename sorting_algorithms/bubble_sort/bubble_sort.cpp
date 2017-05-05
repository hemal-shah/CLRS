#include<iostream>
#include<vector>
int main(int argc, char const *argv[]) {
    std::vector<int> v;
    int n;
    std::cout << "How many elements you want to enter?" << '\n';
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        int temp;
        std::cin >> temp;
        v.push_back(temp);
    }

    for(int i = 0; i < n - 1; i++){
        for(int j = i + 1; j < n; j++){
            if(v[i] > v[j]){
                int temp = v[i];
                v[i] = v[j];
                v[j] = temp;
            }
        }
    }

    std::vector<int>::iterator itr = v.begin();
    while(itr != v.end()){
        std::cout << *itr << ' ';
        itr++;
    }
    std::cout << '\n';

    return 0;
}
