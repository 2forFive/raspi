import vlc
import time
import smbus


bus = smbus.SMBus(1) ## 开启总线
address = 0x48 ## address  ---> 器件的地址(硬件地址 由器件决定)
A0 = 0x40      ##  A0    ----> 器件某个端口的地址（数据存储的寄存器）
A1 = 0x41
A2 = 0x42
A3 = 0x43

check = 0
#光敏电阻:0=没有检测到瓶子 1:有瓶子有标签 2:有瓶子没有标签
#红外对射:3:有东西经过

def loop1():#光敏电阻的循环
    part = 0#现输入值所在范围
    time = 0#重复次数
    T=3#目标次数
    sarttime = time.time()
    while True:
        bus.write_byte(address,A0)  ## 告诉树莓派 你想获取那个器件的那个端口的数据
        value0 =bus.read_byte(address) ## 获得数据
        print(value0)

        time.sleep(0.5)
        if(value0 <= 90):#没有瓶子
            check = 0
            time=0
            part=0
            if(time.time()-startime >= 10):
                destry()
#                break
        elif(value0 >= 160):#有瓶子有标签
            if(part == 1):
                time = time + 1
            else:
                time=1
                part=1
            if(time == T):
                check = 1
                time=0
                part=0
#            break

        elif(value0>100 and value0 <= 110):#有瓶子没标签
            if(part == 2):
                time = time + 1
            else:
                time=1
                part=2
            if(time == T):
                check = 2
                time=0
                part=0
#            print("有瓶子没有标签")
#            break
#        print(value1)
#0：没有检测到瓶子（<=90)
#1：有瓶子有标签(=>160)
#2：有瓶子没有标签(100<X<=110)


def loop2():#红外线的循环
    while True:
        bus.write_byte(address,A1)  ## 告诉树莓派 你想获取那个器件的那个端口的数据
        value1 =bus.read_byte(address) ## 获得数据
        bus.write_byte(address,A2)
        value2 =bus.read_byte(address)
        bus.write_byte(address,A3)
        value3 =bus.read_byte(address)
        
        starttime = time.time()
        
        X = value1
        Y = value2
        Z = value3
        time1 = 0
        time2 = 0
        time3 = 0
        time = 80
        
        while True:
            if(time.time()-starttime >= 10):#一段时间检测不到东西
                check  = 4
#                break
                
            bus.write_byte(address,A1)
            print(bus.read_byte(address))
            if(X == bus.read_byte(address)):#和第一次的X为同一个数值就time++
                time1 = time1 + 1
            if(X != bus.read_byte(address)):#当X和当时读进来的值不同就重新开始循环
                time1 = 0
                X = bus.read_byte(address)
###########
            bus.write_byte(address,A2)
            if(Y == bus.read_byte(address)):
                time2 = time2 + 1
            if(Y != bus.read_byte(address)):
                time2 = 0
                Y = bus.read_byte(address)
############
            bus.write_byte(address,A3)
            if(Y == bus.read_byte(address)):
                time3 = time3 + 1
            if(Y != bus.read_byte(address)):
                time3 = 0
                Y = bus.read_byte(address)
############                
            if(time1 == time|time2 == time|time3 == time):#同一个数值有十次就break
                time1 = 0
                time2 = 0
                time3 = 0
                check=3
                #break
        break

def loop3():
    time = 0
    while True:
        bus.write_byte(address,A0)  ## 告诉树莓派 你想获取那个器件的那个端口的数据
        value0 =bus.read_byte(address) ## 获得数据
        if(value0 <= 90):#没有瓶子
            time = time + 1 
        else:
            time = 0
        if(time == 3):
            check = 0
            break
        
def destroy():
    check = 0
    Num = 0