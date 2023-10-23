import sys

def solotion(nSet,mSet):
    result=sorted(nSet&mSet)
    print(len(result))
    for i in result:
        print(i)
    return result

if __name__=="__main__":
    n, m =map(int,sys.stdin.readline().split())
    nSet=set()
    mSet=set()
    for i in range(n):
        nSet.add(sys.stdin.readline().rstrip())
    for i in range(m):
        mSet.add(sys.stdin.readline().rstrip())
    solotion(nSet, mSet)

    