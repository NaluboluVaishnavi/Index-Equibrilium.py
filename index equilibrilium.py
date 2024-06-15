'''def process_input():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    array = []
    for i in range(1,N + 1):
        array.append(int(data[i]))
        print("N:",N)
        print("Array:",array)
        process_input()'''
a = [2,4,3,1,2,1,2,3]
a = [5,2,1,3,1,2,5]
a = [1,1,1,2,1]
f = 0
for i in range(0,len(a)):
    i1 = i
    j = i+1
    s1=0
    s2=0
    #left side
    while i>=0:
        s1 += a[i]
        i = i-1
    #right side
    while j<len(a):
        s2+=a[j]
        j = j+1
    if s1==s2:
        print(i1+1)
        f=1
        break 
if f==0:
    print(len)
     
