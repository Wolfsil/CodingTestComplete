import sys 


# def solutionFalut(n,m):
#     count2=0
#     count5=0
#     for i in range(m+1,n+1):
#         while i!=0 and i%5==0:
#             i=i//5
#             count5=count5+1
#         while i!=0 and i%2==0:
#             i=i//2
#             count2=count2+1
#     for i in range(1,n-m+1):
#         while i!=0 and i%5==0:
#             i=i//5
#             count5=count5-1
#         while i!=0 and i%2==0:
#             i=i//2
#             count2=count2-1
            
#     if count5>count2:
#         print(count2)
#     else:
#         print(count5)

def solution(n,m): 
    def count(num):
        count2=0
        count5=0
        
        i=5
        while i<=num: 
            count5=count5+(num//i)
            i=i*5
        
        i=2
        while i<=num: 
            count2=count2+(num//i)
            i=i*2
        return (count2, count5) 
    
     
    mother=count(n)
    child1=count(n-m)
    child2=count(m)
    result2 = mother[0]-child1[0]-child2[0]
    result5= mother[1]-child1[1]-child2[1]
    
    if result2>result5:
        print(result5)
    else:
        print(result2)
if __name__=="__main__":
    n,m= map(int,sys.stdin.readline().split())
    solution(n, m)
