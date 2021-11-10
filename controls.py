from pyPS4Controller.controller import Controller
import math
from events import Events
from pymouse import PyMouse
from pykeyboard import PyKeyboard

mouseX=0
mouseY=0
#m = PyMouse()
m = PyMouse()
k = PyKeyboard()

#VARIABLES
left_stick_x=0
left_stick_y=0
right_stick_x=0
right_stick_y=0

#chnges how right stick moves mouse
#0-stick value is transalted into mosue cordinate directly
#1-sticks value is added to current mouse coordinate
mouse_mode=1

#minimal value of stick position change that will move cursor
stickDelta=400

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

#m.click(400+int(mouseX/2000),290+int(mouseY/2000))
def x(var):
    return 400+int(var/120)

def y(var):
    return 280+int(var/120)

def handle_sticks(self):
    global left_stick_x, left_stick_y
    global right_stick_x, right_stick_y
    print("MouseX:"+str(left_stick_x)+" mouseY:"+str(left_stick_y))
    print("MouseX:"+str(right_stick_x)+" mouseY:"+str(right_stick_y))

def left_stick():
    global right_stick_x, right_stick_y
    global left_stick_x, left_stick_y
    global m,k
    global mouseX,mouseY
    global mouse_mode
    print("MouseX:"+str(left_stick_x)+" mouseY:"+str(left_stick_y))
    if( abs(left_stick_x)>29000 or abs(left_stick_y)>29000):
        print("run "+str(max(abs(left_stick_x),abs(left_stick_y))))
        k.press_key(k.control_key)
    else:
        k.release_key(k.control_key)
        #k.tap_key(k.control_key)

    m.click(400+int(left_stick_x/2000),280+int(left_stick_y/2000))
    if(mouse_mode==1 and right_stick_x!=0 and right_stick_y!=0):
        m.move(mouseX,mouseY)





def right_stick():
    global right_stick_x, right_stick_y, m
    global left_stick_x, left_stick_y
    global mouseX,mouseY
    global mouse_mode
    #print("MouseX:"+str(right_stick_x)+" mouseY:"+str(right_stick_y))
    if(mouse_mode==0):
        m.move(400+int(right_stick_x/85),280+int(right_stick_y/120))
    elif(mouse_mode==1):
        mouseX+=int(right_stick_x/5000)
        mouseY+=int(right_stick_y/5000)
        print(str(mouseX)+" | "+str(mouseY))
        mouseX=clamp(mouseX,0,800)
        mouseY=clamp(mouseY,0,600)
        m.move(mouseX,mouseY)




class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        global m,k
        k.press_key(k.control_key)

    def on_x_release(self):
        global m,k
        k.release_key(k.control_key)

    def on_R3_x_at_rest(self):
        global right_stick_x
        right_stick_x=0
        right_stick()
        

    def on_R3_y_at_rest(self):
        global right_stick_y
        right_stick_y=0
        right_stick()

    def on_R3_left(self,value):
        global right_stick_x
        global stickdelta
        if(abs(right_stick_x-value)>stickDelta):
            right_stick_x=value
        right_stick()

    def on_R3_right(self,value):
        global right_stick_x
        global stickdelta
        if(abs(right_stick_x-value)>stickDelta):
            right_stick_x=value
        right_stick()

    def on_R3_up(self,value):
        global right_stick_y
        global stickdelta
        if(abs(right_stick_y-value)>stickDelta):
            right_stick_y=value
        right_stick()

    def on_R3_down(self,value):
        global right_stick_y
        global stickdelta
        if(abs(right_stick_y-value)>stickDelta):
            right_stick_y=value
        right_stick()

    def on_L3_x_at_rest(self):
        global left_stick_x
        left_stick_x=0
        left_stick()

    def on_L3_y_at_rest(self):
        global left_stick_y
        left_stick_y=0
        left_stick()

    def on_L3_left(self,value):
        global left_stick_x
        global stickdelta
        left_stick_x=value
        left_stick()

    def on_L3_right(self,value):
        global left_stick_x
        global stickdelta
        left_stick_x=value
        left_stick()

    def on_L3_up(self,value):
        global left_stick_y
        global stickdelta
        left_stick_y=value
        left_stick()

    def on_L3_down(self,value):
        global left_stick_y
        global stickdelta
        left_stick_y=value
        left_stick()

    def on_L1_press(self):
        global right_stick_x, right_stick_y, m
        global mouseX,mouseY
        global mouse_mode
        if(mouse_mode==0):
            m.click(x(right_stick_x),y(right_stick_y),1)
        elif(mouse_mode==1):
            m.click(mouseX,mouseY,1)

    def on_R1_press(self):
        global right_stick_x, right_stick_y, m
        global mouseX,mouseY
        global mouse_mode
        if(mouse_mode==0):
            m.click(x(right_stick_x),y(right_stick_y),2)
        elif(mouse_mode==1):
            m.click(mouseX,mouseY,2)




controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)

