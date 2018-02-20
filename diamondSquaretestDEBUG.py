'''TESTING DEBUGGING'''

import math 
import random as random

size=0
map=[]
max=0

def Terrain(detail):
	global size;
	size = int(math.pow(2, detail) + 1);
	global max
	max = size - 1;
	#map = new Float32Array(size * size);
	global map
	map=[0 for i in range(size*size)]
	print "Initial Map=%s"%(map)

def get(x, y):
	if x < 0 or x > max or y < 0 or y > max:
		return -1;
	return map[x + size * y];

def set (x, y, val):
	map[x + size * y] = val;
	print "map[%d] = %s"%(x + size * y ,val)
	
	
def generate (roughness):	
	set(0, 0, 999);
	set(max, 0, 999);
	set(max, max, 999);
	set(0, max, 999);
	
	#print "Map=%s"%(map)		
	divide(max,roughness);

totalDivisions=0
def divide(size,roughness):	
	
	global totalDivisions
	totalDivisions+=1
	
	x=y=half= size/2;
	reducedScale = roughness * size;
	
	if half < 1:
		return
				
	print 'Do Diamond Step'
	for y in range (half, max, size):		
		for x in range (half, max, size):
			diamond(x, y, half, 999);
			print "x=%d, y=%d"%(x,y)
	print "Map after Diamond %d Step=%s"%(totalDivisions,map)
	
	print 'Do Square Step'
	for y in range(0, max+1, half):		
		for x in range( (y + half) % size, max+1, size):			
			square(x, y, half, 999)
			print "x=%d, y=%d"%(x,y)
	print "Map after Square %d Step=%s"%(totalDivisions,map)
	
	print 'Divided with size=%d'%(size)			
	divide(size/2, roughness);	
	
        
def average(values):
	#do averaging
	length=len(values)
	#print "length=%f"%(length)
	#print "values=%s"%(values)
	
	average=(values[0]+values[1]+values[2]+values[3]) / 4
	
	#print "average=%f"%(average)
	
	return average
	
def diamond(x, y, size, offset):# upper left	 # upper right	# lower right	# lower left
	ave = average([get(x - size, y - size), get(x + size, y - size),  get(x + size, y + size),  get(x - size, y + size) ]);
	set(x, y, 999);
        
def square(x, y, size, offset):# top	 # right	 # bottom	 # left
	ave = average([  get(x, y - size), get(x + size, y), get(x, y + size),  get(x - size, y) ]);
	set(x, y, 999);

'''    
  def draw (ctx, width, height) {
     self = this;
     waterVal = size * 0.3;
    for ( y = 0; y < size; y++) {
      for ( x = 0; x < size; x++) {
         val = get(x, y);
         top = project(x, y, val);
         bottom = project(x + 1, y, 0);
         water = project(x, y, waterVal);
         style = brightness(x, y, get(x + 1, y) - val);
        rect(top, bottom, style);
        rect(water, bottom, 'rgba(50, 150, 200, 0.15)');
      }
    }
    function rect(a, b, style) {
      if (b.y < a.y) return;
      ctx.fillStyle = style;
      ctx.fillRect(a.x, a.y, b.x - a.x, b.y - a.y);
    }
    function brightness(x, y, slope) {
      if (y === max or x === max) return '#000';
       b = ~~(slope * 50) + 128;
      return ['rgba(', b, ',', b, ',', b, ',1)'].join('');
    }
    function iso(x, y) {
      return {
        x: 0.5 * (size + x - y),
        y: 0.5 * (x + y)
      };
    }
    function project(flatX, flatY, flatZ) {
       point = iso(flatX, flatY);
       x0 = width * 0.5;
       y0 = height * 0.2;
       z = size * 0.5 - flatZ + point.y * 0.75;
       x = (point.x - size * 0.5) * 6;
       y = (size - point.y) * 0.005 + 1;
      return {
        x: x0 + x / y,
        y: y0 + z / y
      };
    }
  };
'''     

terrain = Terrain(2)
generate(0.7);

#terrain.draw(ctx, width, height);
      
#</script>

