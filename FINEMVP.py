def count8():
    cnt =0
    for i in range(1,10001):
        cnt += str(i).count('8')
    return cnt

def count8_1(sum=0, n=1):
    if n>4: return sum
    sum = sum*10 + 10**(n-1)
    return count8_1(sum,n+1)

def count8_2():
    cnt =0
    cur =1
    while cur <=4:
        cnt = (cnt *10+ 10**(cnt-1))
        cur = cur+1
    return cnt