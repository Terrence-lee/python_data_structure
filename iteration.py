from pythonds.basic import Stack
from pythonds.basic import Queue
import time
problemqueue=Queue()
problemstack=Stack()
onenum=1
zeronum=0
m=0
problemlist=[]
num=0

def initialize(problemlist):
    global problemqueue
    for element in problemlist:
        problemqueue.enqueue(element)

def func(i,q,problemlist):#i+1控制深度；q代表元素的个数
    global onenum #1的次数记录（push）
    global zeronum #0的记录（pop）
    global m #控制输出的临时变量
    if i == q:
        mylist[i-1]=0
        if m%2 == 0:   #Q:为什么这里不除以2就会出现一样的列表显示两次的情况？
            #print(mylist)
            print(m//2+1,end=' ')
            #f1.write(str(int(m/2+1)))
            for j in mylist:
                if j==0:
                    print(problemstack.pop(),end='')
                    #f1.write(problemstack.pop())
                if j==1:
                    problemstack.push(problemqueue.dequeue())
            print(" ",end="")
            #f1.write(" ")
            if (m+12)%5==0:
                print("\n") #格式
                #f1.write("\n")
            initialize(problemlist)

        m+=1
        return
    elif onenum>=zeronum and onenum<num+1 and zeronum<num+1:
        mylist[i]=1
        onenum+=1# 1的个数
        func(i+1,q,problemlist)
        onenum-=1 #递归恢复
        mylist[i]=0 #赋值为0
        zeronum+=1 #0的个数
        func(i+1,q,problemlist)
        zeronum-=1

def myinput():
    global problemlist
    global num
    num=eval(input("how many elements do you want?"))
    for i in range(num):
        problemlist.append(chr(65+i))

starttime=time.time()
myinput()
mylist=[0]*2*num
mylist[0]=1
#f1=open('number_record.txt','r+')
initialize(problemlist)
func(1,2*num,problemlist)
endtime=time.time()
print("\n")
print("time:{}".format(endtime-starttime))
#f1.close()




