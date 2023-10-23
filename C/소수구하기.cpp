#include <iostream>
#include <cmath>
#define len 1000001
using namespace std;
int main() {
	int a, b;
	bool array[len] = {false};
	cin >> a >> b ;
	if (a == 1) a = 2;

	for (int i = 2; i <= sqrt(b); i++) {
		if (array[i] == true)continue;
		for (int j = i + i; j < len; j += i) {
			array[j] = true;
		}
	}
	for (int i = a; i <= b; i++) {
		if (array[i] != true) cout << i <<"\n";
	}


	return 0;
}
