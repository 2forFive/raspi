import RPi.GPIO as GPIO
import time

ObstaclePin = 12  
check = 0

def setup():
    GPIO.setmode(GPIO.BCM)       
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        time.sleep(1)
        if (0 == GPIO.input(ObstaclePin)):  #当检测到障碍物时，输出低电平信号
            print ("Detected Barrier!")
            check = 1
        else :
            print ("****Nothing!******")
            

def destroy():
    GPIO.cleanup()                    

if __name__ == '__main__':     
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()