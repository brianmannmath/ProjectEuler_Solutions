#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>

int tri(int n){
  return (n+1)*n/2;
}


  

int main() { 

  //import the array of numbers
  std::ifstream input("triangle.txt");
  std::vector<int> data;
  int a;
  //creates a vector of values from the triangular array
  for(int i = 0; i < tri(100); i++){
    input >> a;
    data.push_back(a);
  }

  for(int i = 98; 0 <= i; i--){
    for(int j = 0; j < i+1; j++){
      data.at(tri(i) + j) = data.at(tri(i) + j) + std::max(data.at(tri(i+1) + j) ,data.at(tri(i+1) + j + 1));
    }
  }

  std::cout << data.at(0) << '\n';

  return 0;
    
  

}
