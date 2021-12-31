import PhotoresistorAndInfrared as oj
#import Infrared as oj2

check = 0
#check=1 瓶子本身无瓶标、标签掉落完成  check=0瓶子还不能进入储存处
'''def setup():
    oj2.setup()'''
    
def loop():
#    oj.loop3()
    oj.loop3()
#    oj.loop2()
    check = 1
    
def destroy():
    check = 0
    oj.destroy()
#    oj2.destroy()
    
if __name__ == '__main__':     
#    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()