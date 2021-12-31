import RPi.GPIO as GPIO
import time

ObstaclePin = 12  
check2 = 0
#0：没有东西经过 1：有东西经过

def setup():
    GPIO.setmode(GPIO.BCM)       
#    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ObstaclePin, GPIO.IN)
def loop():
    StartTime = time.time()
    while True:
#        if(time.time()-StartTime >= 5):
#            break
    #防止瓶身本来就没有标签而一直检测不到瓶标的掉落


        if (0 == GPIO.input(ObstaclePin)):  #当检测到障碍物时，输出低电平信号
            print ("Detected Barrier!")
            check2 = 1
            
        else :
            print ("****Nothing!******")

#        time.sleep(0.5)


def destroy():
    GPIO.cleanup()
    check2 = 0

'''if __name__ == '__main__':     
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()'''