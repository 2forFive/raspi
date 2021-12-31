import RPi.GPIO as GPIO
import time

s0 = 21
s1 = 22
s2 = 23
s3 = 24
signal = 25
NUM_CYCLES = 2000
nred = 0
nblue = 0
ngreen = 0
n = 0


def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#   GPIO.setup(s0,GPIO.OUT,initial=GPIO.HIGH)
#   GPIO.setup(s1,GPIO.OUT,initial=GPIO.LOW)
  GPIO.setup(s2,GPIO.OUT)
  GPIO.setup(s3,GPIO.OUT)
  print("\n")
  

def loop():
  temp = 1
  while(1):
    global n , nred , nblue , ngreen
    n = n + 1
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start 
#    red  = NUM_CYCLES / duration / 170
    red  = NUM_CYCLES / duration
    nred = (nred + red/255) 
   
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
#    blue = NUM_CYCLES / duration / 190
    blue = NUM_CYCLES / duration
    nblue = (nblue + blue/255) 

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
#    green = NUM_CYCLES / duration /162
    green = NUM_CYCLES / duration
    ngreen = (ngreen + green/255)  
    
    
    print("red",red,"\n","green",green,"\n","blue",blue)
    print("nred",nred/n,"\n","ngreen",ngreen/n,"\n","nblue",nblue/n)
#     if green<7000 and blue<7000 and red>12000:
#       print("red")
#       temp=1
#     elif red<12000 and  blue<12000 and green>12000:
#       print("green")
#       temp=1
#     elif green<7000 and red<7000 and blue>12000:
#       print("blue")
#       temp=1
#     elif red>10000 and green>10000 and blue>10000 and temp==1:
#       print("place the object.....")
#       temp=0


def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    
    setup()

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()