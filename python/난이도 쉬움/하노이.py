import sys

def hanoi(cout,start, mid ,target ):
    if cout<=1:
        print(start, target)
        return
    hanoi(cout-1,start, target, mid)
    print(start, target)
    hanoi(cout-1, mid, start, target)

def solution(N):
    hanoi(N,1,2,3)
    
if __name__=="__main__":
    scan=sys.stdin.readline().rstrip()
    solution(int(scan))    
