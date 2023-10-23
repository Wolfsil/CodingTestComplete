

if __name__=="main":
    limit =10001

    arr=[False for i in range(limit)]

    for number in range(1,limit):
        result=number
        while number>0:
            result+=number%10
            number=number//10
        if result<limit:  arr[result] =True
    for i in range(1,limit):
        if arr[i]==False: print(i)
    