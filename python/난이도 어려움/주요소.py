import sys 

def solution(n,road, gas):
    fuel=0
    index=0
    n=n-1
    while n>index:
        checker=index
        while n> checker and gas[index]<=gas[checker]:
            fuel=(gas[index]*road[checker])+fuel
            checker=checker+1
        index=checker
    print(fuel)
    return fuel

            
if __name__=="__main__":
    n= int(sys.stdin.readline())
    road=list(map(int, sys.stdin.readline().split()))
    gas=list(map(int, sys.stdin.readline().split()))
    if len(road)!=n-1 or len(gas)!=n:
        print("INPUT ERROR")
    else:
        solution(n,road,gas)
        
    