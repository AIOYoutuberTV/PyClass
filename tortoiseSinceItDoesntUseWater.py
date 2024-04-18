import turtle as tortoise

#Since Py provides no public/local var sytem, I've made my own.

colourStart = 0xFFA516
colourEnd = 0xFF170F 
colourDiff = 0x8E07//20 #For whatever reason python stores these as int in decimal... Okay???

def hexToColourCode(inColour): #Takes the int data and turns it into a string with the format usable by the tortoise.
	return("#"+(hex(inColour)[2:]))

tortoise.width(5)
tortoise.color(hexToColourCode(colourStart))
tortoise.up();tortoise.setx(-350);tortoise.down()
while colourStart != colourEnd:
	tortoise.forward(2)
	tortoise.color(hexToColourCode(colourStart-colourDiff)) 
tortoise.done()

#TODO: Figure out whatever is going on here