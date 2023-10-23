from random import randint
import sys

size=10001

#딕셔너리법을 쓰면 메모리 절약이 되고 범위도 상관없어지지 않을까란 생각을 했지만
#범위가 정해져 있는 문제에선 최악의 경우 메모리 사용량 두배이므로....
def sort(arr):
    
    temp= [0 for _ in range(size)]
    result=[]
    for i in arr:
        temp[i]=temp[i]+1
    for i in range(len(temp)):
        for j in range(temp[i]):
            result.append(i)
    return result

if __name__=="__main__":
    size=int(sys.stdin.readline())
    arr=[]
    for i in range(size):
        arr.append(int(sys.stdin.readline()))
   
    sort(arr)

    