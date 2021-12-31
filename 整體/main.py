import PhotoresistorAndInfrared as Detect #检测程序
import serial #通信
import sys #UI
from PyQt5.QtWidgets import * #UI
import jm1 as ui #UI
import #各种库

def setup():#将各种参数初始化、同时将交互窗口调出
    #检测程序的初始化
    Detect.check1 = 0
    Detcet.check2 = 0
    
    #窗口的
    app = QApplication(sys.argv)
    myMainWindow = QMainWindow()
    myUi = jm1.Ui_MainWindow()
    
    #通信的初始化
    uart1 = serial.Serial(port = "/dev/ttyAMA0", baudrate = 115200)
    uart1.flushInput()

def loop():
    #这里并不是true，这个循坏的开始需要用户点击开始投瓶，所以要有一个返回值让这个循环开始
    #这个loop中只要用户点了“我投完了”，就要break。但目前不知道怎么实现
    while True:
        
        #让电热笔开始加热,让推动瓶子的摩擦轮开始工作,让光敏电阻开始工作,挡板挡住通道
        uart1.write("".encode("utf-8"))#推动摩擦轮开启,这里的摩擦刘要一直转么？可能前面的瓶子还没处理好，后面的瓶子又投进来了怎么办？
        uart1.write("".encode("utf-8"))#挡板舵机,挡板挡道
        #差电热笔
        Detect.loop1()#光敏电阻
        
        #当光敏电阻的loop跳出后，加热笔舵机就可以开始转动
        uart1.write("".encode("utf-8"))#加热笔舵机-切割瓶标
        #一定时间后
        uart1.write("".encode("utf-8"))#加热笔舵机-归位
        
        #切割完成，瓶标摩擦轮转动,同时红外线对射装置开始工作,
        uart1.write("".encode("utf-8"))#瓶标摩擦轮转动
        Detect.loop2()#红外线对射装置
        
        #当红外线检测loop完成后，停止瓶标摩擦轮，释放挡板，开启后端摩擦推进轮
        uart1.write("".encode("utf-8"))#瓶标摩擦轮停止
        uart1.write("".encode("utf-8"))#释放挡板
        uart1.write("".encode("utf-8"))#后端摩擦推进轮转动
        
    '''uart1 = serial.Serial(port = "/dev/ttyAMA0", baudrate = 115200)
    uart1.write("i am".encode("utf-8"))
    count = uart1.
    uart1.read()'''
    