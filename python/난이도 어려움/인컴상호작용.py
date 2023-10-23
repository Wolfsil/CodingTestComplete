import sys

#일반풀이
def solution(n,m,arr):
    result=[]
    for i in range(m):
        count=0
        search=arr[i]
        for i in range(search[1],search[2]+1):
            if n[i] == search[0]:
                count=count+1
        result.append(count)
    for i in result:
        print(i)  
             
#향상풀이
def solution2(n,m,arr):
    result=[]
    memo=[[0 for i in range(26)] for j in n]
    #행: 순서, 열:알파벳
    ask=ord('a')
    for i in 'abcdefghijklmnopqrstuvwxyz':
        target=ord(i)-ask
        count=0
        for j in range(len(n)):
            if n[j]==i:
                count=count+1
            memo[j][target]=count
        
    for i in arr:
        targetChar=ord(i[0])-ask
        targetStart=i[1]-1
        targetEnd=i[2]
        if targetStart<0:
            result.append(memo[targetEnd][targetChar])
        else:    
            result.append(memo[targetEnd][targetChar]-memo[targetStart][targetChar])
             
    for i in result:
        sys.stdout.write(str(i)+"\n")
        
    return result   

if __name__=="__main__":
    n= sys.stdin.readline().rstrip()
    m= int(sys.stdin.readline())
    arr=[]
    for i in  range(m):
        temp= sys.stdin.readline().split()
        temp[1]=int(temp[1])
        temp[2]=int(temp[2])
        arr.append(temp)
    
    solution2(n,m, arr)
