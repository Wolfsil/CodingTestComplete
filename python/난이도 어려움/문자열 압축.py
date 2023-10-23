import sys

def solution(s):
    length=len(s)
    minimum=length

    for size in range(1,length//2):
        short_size=length
        cut=""
        count=0

        for start in range(0,length+1,size):
            check=s[start:start+size]
            if cut==check:
                short_size=short_size-size
                count+=1
            else:
                cut=check
                while count != 0:
                    #1을 안더해주면 100,1000같은 경우엔 2,3자리가됨. 반면 991,99는 정상 동작
                    #0~9까지의 범위가 아니라, 1~10까지의 범위로 재조정
                    count+=1
                    short_size+=1
                    count//=10
                    
        while count != 0: 
            count+=1 
            short_size+=1
            count//=10        
            
             
        if short_size<minimum:
            minimum=short_size
            
    print("answer: ",minimum)

if __name__=="__main__":
    # scan=sys.stdin.readline
    # solution(scan().rstrip())    
    solution("asd"*100)  
