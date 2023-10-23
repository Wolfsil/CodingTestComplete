#include <iostream>
#include <string>


using namespace std;
int main() {
	string input;
	int alpha[26] = { 0, };
	int maximum = 0;
	int second = 0;
	char result='?';
	cin >> input;

	for (int i = 0; i < input.length(); i++) {
		int size= ++alpha[toupper(input[i])-'A'];
		if (size >= maximum) {
			second = maximum;
			maximum = size;
			result = input[i];
		}
	}
	if (maximum == second)  cout << "?";
	else cout << char(toupper(result));
	return 0;
}