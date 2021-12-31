
import vlc
import time
import smbus


bus = smbus.SMBus(1) ## 开启总线
address = 0x48 ## address  ---> 器件的地址(硬件地址 由器件决定)
A0 = 0x40      ##  A0    ----> 器件某个端口的地址（数据存储的寄存器）
A1 = 0x41
A2 = 0x42
A3 = 0x43

def loop():
    while True:
        bus.write_byte(address,A0)  ## 告诉树莓派 你想获取那个器件的那个端口的数据
        value =bus.read_byte(address) ## 获得数据
        print(value)
        time.sleep(0.5)

def destroy():
    check = 0

def loop5():
    Time = 0
    T = 10
    starttime = time.time()
    while True:
        if(time.time()-starttime >= 10):#一段时间检测不到东西
            check  = 4
#            break
        bus.write_byte(address,A1)
        value = bus.read_byte(address)
        print(value)
        if(value>=80):
            Time = Time + 1
        if(Time >= T ):
            check = 3
            break
            print("red out")
            

if __name__ == '__main__':     
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
