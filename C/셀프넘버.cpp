#include <iostream>
#define limit 10001

using namespace std;

int main() {
	bool arr[limit] = {false};
	for (int i = 1; i < limit; i++) {
		int result=i;
		for (int j=i; j > 0; j /= 10) {
		
			result += (j % 10);
		}
		if (result <limit) arr[result] = true;
	}
	for (int i = 0; i < limit; i++) {
		if(arr[i]==false)	cout << i<<"\n";
	}
	return 0;
}