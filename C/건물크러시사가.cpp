#include <string>
#include <vector>
#include <iostream>
using namespace std;
//행열:n,m(1000이하)
//스킬: 250,000 이하, [적아군, x1,y1,x2,y2,힘]
int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    int n=board.size();
    int m = board[0].size();

    for (int i = 0; i < skill.size(); i++) {
        int power= skill[i][5];
        if (skill[i][0] == 1)power = -power;
        areaChange(board, skill[i][1], skill[i][2], skill[i][3], skill[i][4], power);
    }
    
    return returnAnswer(board);
}
void areaChange(vector<vector<int>>& board,int x1,int y1, int x2,int y2, int power) {

    for (int i = x1; i <= x2; i++) {
        for (int j = y1; j <= y2; j++) {
            board[i][j] += power;
        }
    }

}
int returnAnswer(vector<vector<int>>& board) {
    int count = 0;
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[i].size(); j++) {
            if (board[i][j] > 0) {
                count++;
            }
        }
    }
    return count;
}