import sys
import pprint
import readchar
from typing import Dict,Tuple
sys.path.append('/mnt/ssd1/PROJECTS/PYTHON-PROJECT/pconsole/')
from console import Console 

class HexMap(Dict[tuple,int]):
    Size=(10,10)

    def __init__(self):
        pass

    def Render(self):
        Console.Clear();
        for y in range(self.Size[0]):
            if( y % 2 == 1 ):
                Console.Write("_");
            for x in range(self.Size[0]):

                Console.Write(f"|{self.Tile((x,y))}")
            Console.Write("\n")
    
    def Tile(self,p):
        if( p not in self.keys() ):
            return "_"
        return "."



print("OK!")

h=HexMap()

h.Render()

key=readchar.readkey()

if(key==readchar.key.DOWN):
    print("Down")
if(key==readchar.key.UP):
    print("UP")
if(key==readchar.key.LEFT):
    print("LEFT")
if(key==readchar.key.RIGHT):
    print("RIGHT")

print(f"K={key}")
#c=readchar.readchar()
