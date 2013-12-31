#include <fstream>
#include <iostream>
#include <vector>

long vertSum(int *arr, int p){
  long sum = (*(arr + p))*(*(arr + 20 + p))*(*(arr + 40 + p))*( *(arr + 60 +p));

  return sum;
}

long horSum(int *arr, int p){
  long sum = (*(arr + p))* ( *(arr + p + 1)) *( *(arr + p + 2)) *( *(arr + p + 3));

  if(p % 20 > 16){
    return 0;
  }

  return sum;
}

long diagSum(int *arr, int p){

  if(p % 20 >16){
    return 0;
  }

  long sum = (*(arr + p))*( *(arr + 21 + p))*( *(arr + 42 + p))*( *(arr + 63 + p));

  return sum;
}

long ldiagSum(int *arr, int p){

  if(p % 20 < 3){
    return 0;
  }

  long sum = (*(arr + p))*(*(arr + 19 + p))*(*(arr+ 38 + p))*(*(arr + 57 + p));

  return sum;
}



int main(){
  int arr[400];
  
  std::ifstream input("number.txt");
  for(int i = 0; i < 400; i++){
    input >> arr[i];
  }

  long max = 0;

  for(int i = 0; i < 400; i++){
    if(horSum(arr,i) > max){
      max = horSum(arr,i);
    }
  }

  for(int i = 0; i < 340; i++){
    if(vertSum(arr,i) > max){
      max = vertSum(arr,i);
    }
  }

  for(int i = 0; i < 340; i++){
    if(diagSum(arr,i) > max){
      max = diagSum(arr,i);
    }
  }

  std::cout << max << "\n";

  for(int i = 0; i < 340; i++){
    if(ldiagSum(arr,i) > max){
	max = ldiagSum(arr,i);
      }
  }

  std::cout << max << "\n";

return 0;

}
