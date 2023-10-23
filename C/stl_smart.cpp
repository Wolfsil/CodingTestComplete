#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <stack>
#include <queue>
#include <stdio.h>
#include <algorithm>
using namespace std;

class test {
public:
	int id = 0;
	test(int id) :id(id) {}
	~test() {
		cout << "test 소멸" << id << endl;
	}
	void sPtr() {

	}
	bool operator <(test b) const{
		return this->id < b.id;
	}
};
int main()
{
	/*
	vector<int> vec;
	int size = 10;
	cout << "사이즈: ";
	scanf_s("%d", &size);
	cout << "#벡터#";
	for (int i = 0; i < size; i++) {
		vec.push_back(i);
	}
	sort(vec.begin(), vec.end());
	for (int i = 0; i < size; i++) {
		cout << vec.at(i)<<vec[i] << "\n";
	}
	*/
	
	/*
	cout << "#스트링#" << "\n문자열: ";
	string a;
	char* b = (char*)"10";
	cin >> a;
	for (int i = 0; i < a.length(); i++) {
		cout << a[i];
	}
	cout << "어팬드(안녕): " << a.append("hello\n") << "\n";
	cout << "stoi 사용법: " << stoi(b) << "\n";
	cout << "문자열 길이: " << to_string(a.length()) << "\n";
	
	b = (char*)a.c_str();
	for (int i = 0; i < strlen(b); i++) {
		cout << ".." << b[i] << "\n";
	}
	cout << b;
	*/

	/*
	set<string> se;
	se.insert("가지");
	se.insert("다리미");
	se.insert("나나미");
	se.insert("바브리움");
	se.insert("라라랜드");
	se.insert("사형");
	for (string a : se) {
		cout << a<<"\n";
	}
	*/

	/*
	stack<test> stac;
	stac.push(test(10));
	stac.push(test(20));
	cout << stac.top().id;
	stac.pop();
	cout << stac.top().id;
	*/
	/*
	queue<test> qu;
	qu.push(test(10));
	qu.push(test(20));
	cout << qu.front().id;
	qu.pop();
	cout << qu.front().id;
	*/
	/*
	priority_queue<test> qu;
	qu.push(test(10));
	qu.push(test(100));
	qu.push(test(20));
	cout << qu.top().id;
	qu.pop();
	cout << qu.top().id;
	return 0;
	*/

	/*
	unique_ptr<test> pTest(new test(0));
	pTest = unique_ptr<test>(new test(1));
	unique_ptr<test> pTest2=move(pTest);
	cout << "1: " << pTest.get() <<"    2: " <<pTest2->id<< "\n";
	*/
	
	shared_ptr<test> pTest(new test(1));
	shared_ptr<test> pTest2(pTest);
	cout << pTest.use_count() << pTest2.use_count() << "///////" << pTest->id<<endl;

	weak_ptr<test> weak = pTest;
	cout << weak.lock()->id;
	return 0;
}

