from random import randint
import turtle as tortoise
import colorsys
#Since Py provides no public/local var sytem, I've made my own.

colourStart = 0xFFA516
colourEnd = 0xFF170F 
#colourDiff = 0x8E07//20 #For whatever reason python stores these as int in decimal... Okay???
#Why

def hexToColourCode(inColour): #Takes the int data and turns it into a string with the format usable by the tortoise.
        #use string formatting instead
        print("#{:06x}".format(inColour))
        return("#{:06x}".format(inColour))

#Helper Functions
def tupleToColorInt(tuple):
        print(tuple)
        return int(tuple[0]*256)*0x10000+int(tuple[1]*256)*0x100+int(tuple[2]*256)

def HSVToColorCode(hue,saturation,value):
        print(hue,saturation,value)
        return hexToColourCode(tupleToColorInt(colorsys.hsv_to_rgb(hue,saturation,value)))

def RGBToHSV(HexCode):
	return colorsys.rgb_to_hsv(HexCode/0x10000%0x100/0x100,HexCode/0x100%0x100/0x100,HexCode%0x100/0x100)

def HSVInterpol(a,b,f):
        print(f)
        c = [0,0,0]
        for i in range(3):
            c[i] = a[i]+(b[i]-a[i])*f
        return c

def incrementWidth(width):
       return width + 1

hsvStart = RGBToHSV(colourStart)
hsvEnd = RGBToHSV(colourEnd)


#Length of this object, should(must) be divisible by step
length = 300

#Step Distance
step = 5

tortoise.bgcolor("black")

for i in range(100):
        tortoise.color("white")
        tortoise.up()
        tortoise.speed(100)
        tortoise.goto(randint(-350,350),randint(-350,350))
        tortoise.down()
        tortoise.dot(randint(1,5))

iterations = int(length/step)

tortoise.width(5)
tortoise.color(HSVToColorCode(*hsvStart))
tortoise.up();tortoise.setx(-320);tortoise.sety(20);tortoise.down()
tortoise.right(45)
for i in range(iterations):
        
        hsvCurrent = HSVInterpol(hsvStart,hsvEnd,(i+1)/iterations)
        
        tortoise.forward(step)
        tortoise.color(HSVToColorCode(*hsvCurrent))
        tortoise.width(incrementWidth(tortoise.width()))
        tortoise.left(0.2)

tortoise.up();tortoise.left(45);tortoise.back(8);tortoise.forward(17);tortoise.right(180);tortoise.right(90);tortoise.forward(24);tortoise.left(90);tortoise.left(22.5);tortoise.forward(10);tortoise.right(22.5);tortoise.down()
tortoise.width(10)
tortoise.color("white")
tortoise.begin_fill()
tortoise.circle(20)
tortoise.end_fill()
tortoise.done()