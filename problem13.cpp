#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<stdio.h>
#include<vector>
#include<cmath>

int main(){
  
  std::ifstream input("numbers13.txt");
  int arr[5000];
  int i = 0;
  
  while(input.good()){
    char c[1];
    c[0] = input.get();
    if(c[0] != '\n'){
      int a = atoi(c);
      arr[i] = a;
      i++;
    }
  }

  long sum = 0;
  int k = 0;

  for(int j = 49; 0 <= j; j--){
    for(int i = 0; i < 100; i++){
      if(sum > 9999999999){
	sum = sum/10;
	k++;
	sum = sum + pow(10,50-j-1)*arr[50*i + j]/pow(10,k);
      }
      else
	sum = sum + pow(10,50-j-1)*arr[50*i + j]/pow(10,k);
    }
  }
  
  std::cout << sum;   
  

  return 0;

}

  
  

  

