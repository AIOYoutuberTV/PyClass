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

hsvStart = RGBToHSV(colourStart)
hsvEnd = RGBToHSV(colourEnd)



#Length of this object, should(must) be divisible by step
length = 20

#Step Distance
step = 2


iterations = int(length/step)

tortoise.width(5)
tortoise.color(HSVToColorCode(*hsvStart))
tortoise.up();tortoise.setx(-350);tortoise.down()
for i in range(iterations):
        
        hsvCurrent = HSVInterpol(hsvStart,hsvEnd,(i+1)/iterations)
        
        tortoise.forward(step)
        tortoise.color(HSVToColorCode(*hsvCurrent))
	
tortoise.done()
