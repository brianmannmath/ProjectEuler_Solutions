#include<iostream>
#include<fstream>
#include<cmath>
#include<vector>
#include<map>

long numOfFactors(long n, std::map<long, long> map){
  int c = 0;
  for(int i = 1; i <= n/2; i++){
    if(map.count(i) == 1){
      c = c  + map.at(i);
    }
    else


int main() {
  std::map<long, long> map;
  map.insert(std::map<long,long>::value_type(1,1));

  long i = 3;
  long j = 3;
 
  do{
    i = i+j;
    map.insert(std::map<long, long>::value_type(i,numOfFactors(i,map)));
    j++;
  }while(map.at(i) <= 200);

  std::cout << i << ' ' << map.at(i);
    
  return 0;
}
