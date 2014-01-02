// test.cpp : Defines the entry point for the console application.
//

#include<iostream>
#include<vector>
#include<unordered_map>


// Does Collatz but checks to see if the intermediate steps already have values known.

long numberOfSteps(long n, std::unordered_map<long, long> (&vec)){
	long c = 0;
	long s = n;

	while (s != 1){
		if ((s % 2) == 0){
			s = s / 2;
			c++;
			if (s < n){
				return (vec[s] + c);
			}
		}
		else if(s%2 != 0){
			s = (3 * s + 1);
			c++;
			if (s < n){
				return (vec[s] + c);
			}
		}
	}
	return c;
}

int main(){
	long k = 0;
	long f = 0;

	std::unordered_map<long, long> memSteps;
	memSteps[1] = 0;

	//Lists the number and number of steps to get to 1
	for (long i = 2; i <= 1000000; i++){		
		
		if (k < numberOfSteps(i, memSteps)){
			k = numberOfSteps(i, memSteps);
			f = i;
		}
		memSteps[i] = numberOfSteps(i, memSteps);
	}

	std::cout << "Number " << f << " Steps: " << k << "\n";


	return 0;
}

