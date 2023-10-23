#include <vector>
#include <iostream>
using namespace std;

int answer = 1;

void dfs(int now, int w, int s, vector<int> avail, vector<int> info, vector<vector<int>> v) {
    int animal = info[now];
    if (!animal) s++;
    else w++;
   
    if (w >= s) return;

    answer = max(answer, s);
    for (int i = 0; i < avail.size(); i++) {
        vector<int> next = avail;
        next.erase(next.begin() + i);
        for (int j = 0; j < v[avail[i]].size(); j++)
            next.push_back(v[avail[i]][j]);
        dfs(avail[i], w, s , next, info, v);
    }

}


int solution(vector<int> info, vector<vector<int>> edges) {
    vector<vector<int>> v(info.size());

    //[출발, 몇번째 아들]=도착
    for (int i = 0; i < edges.size(); i++)
        v[edges[i][0]].push_back(edges[i][1]);

    //갈 수 있는 노드
    vector<int> avail;
    for (int i = 0; i < v[0].size(); i++)
        avail.push_back(v[0][i]);

    dfs(0, 0, 0, avail, info, v);


    return answer;
}

int main() {
    vector<vector<int>> edges= {{0, 1}, {0, 2}, {1, 3}, {1, 4}, {2, 5}, {2, 6}, {3, 7}, {4, 8}, {6, 9}, {9, 10}};
    vector<int> info={ 0,1,0,1,1,0,1,0,0,1,0 };

    solution(info, edges);
    
    cout << answer;
}