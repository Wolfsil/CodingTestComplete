import sys

def solution(n,arr):
    arr=sorted(arr,key=lambda x:(x[1],x[0]))
    end=arr[0][1]
    count=1
    
    for i in range(1,n):
        if end<=arr[i][0]:
            count=count+1
            end=arr[i][1]

    print(count) 
    return count       
    

            
if __name__=="__main__":
    n=int(sys.stdin.readline())
    arr=[]
    for i in range(n):
        arr.append(tuple(map(int,sys.stdin.readline().split())))
    solution(n,arr)