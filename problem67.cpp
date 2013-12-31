#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>

int tri(int n){
  return (n+1)*n/2;
}

//functions for returning the right and left sub-triangle

std::vector<int> left(std::vector<int> data, int k){
  std::vector<int> dataL;
  
  for(int i = 1; i <= k; i++){
    for(int j = 0; j <= i-1; j++){
      dataL.push_back(data.at(tri(i) + j));
    }
  }
  return dataL;
}

std::vector<int> right(std::vector<int> data, int k){
  std::vector<int> dataR;
  
  for(int i = 1; i <= k; i++){
    for(int j = 1; j <= i; j++){
      dataR.push_back(data.at(tri(i) + j));
    }
  }
  return dataR;
}

int sum(std::vector<int> data, int N){
  if(data.size() == 1)
    return data.at(0);
  else
    return data.at(0) + std::max(sum(left(data,N-1),N-1),sum(right(data,N-1),N-1));
}

  

int main() { 

  //import the array of numbers
  std::ifstream input("triangle.txt");

  //define the tree in the problem using class node
  std::vector<int> data;
  int a;
  
  //creates a vector of values from the triangular array
  for(int i = 0; i < tri(100); i++){
    input >> a;
    data.push_back(a);
  }

  for(int i = 98; 0 <= i; i--){
    for(int j = 0; j <= i; j++){
      int r = tri(i) + j;
      if(data.at(r + i + 1) < data.at(r + i + 2)){
	data.at(r) = data.at(r) + data.at(r + i + 2);
      }
      else
	data.at(r) = data.at(r) + data.at(r + i + 1);
    }
  }

  std::cout << data.at(0);

  return 0;
}
