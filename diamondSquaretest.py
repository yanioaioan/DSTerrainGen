import math 
import random as random
import maya.cmds as cmds

size=0
map=[]
max=0

def InitGrid(divisions):
	global size;
	size = int(math.pow(2, divisions) + 1);
	global max
	max = size - 1;
	#map = new Float32Array(size * size);
	global map
	map=[0 for i in range(size*size)]
	#print "Initial Map=%s"%(map)

def queryArrayElement(x, y):
	if x < 0 or x > max or y < 0 or y > max:
		return -1;
	return map[x + size * y];

def editArrayElement (x, y, val):
	map[x + size * y] = val;
	#print "map[%d] = %s"%(x + size * y ,val)
	
	
def GenGrid (variation):	
	editArrayElement(0, 0, max);
	editArrayElement(max, 0, max / 2);
	editArrayElement(max, max, 0);
	editArrayElement(0, max, max / 2);
	
	#print "Map=%s"%(map)		
	
	random.seed(4)
	SubDivide(max,variation);
	
divisions=0
def SubDivide(size,variation):	
	
	global divisions
	divisions+=1
	
	x=y=halfsize= size/2;
	reducedScale = variation * size;
	
	if halfsize >= 1:			
			
		for y in range (halfsize, max, size):
			for x in range (halfsize, max, size):
				square(x, y, halfsize, random.random() * reducedScale * 2 - reducedScale);	
				
		#print "Map after Square %d =%s"%(divisions,map)
		
		for y in range(0, max+1, halfsize):
			for x in range( (y + halfsize) % size, max+1, size):
				diamond(x, y, halfsize, random.random() * reducedScale * 2 - reducedScale)	
		#print "Map after Diamond %d =%s"%(divisions,map)
		
		print 'SubDivided with size=%d'%(size)			
		SubDivide(size/2, variation);	
		
	else:
		#terminate recursion
		return
        
def avgElements(values):
	#do averaging
	length=len(values)
	#print "length=%f"%(length)
	#print "values=%s"%(values)	
	avg=(values[0]+values[1]+values[2]+values[3]) / 4	
	#print "avgElements=%f"%(avg)	
	return avg
	
def square(x, y, size, offset):# upper left	 # upper right	# lower right	# lower left
	tmpAverage = avgElements([queryArrayElement(x - size, y - size), queryArrayElement(x + size, y - size),  queryArrayElement(x + size, y + size),  queryArrayElement(x - size, y + size) ]);
	editArrayElement(x, y, tmpAverage + offset);
        
def diamond(x, y, size, offset):# top	 # right	 # bottom	 # left
	tmpAverage = avgElements([  queryArrayElement(x, y - size), queryArrayElement(x + size, y), queryArrayElement(x, y + size),  queryArrayElement(x - size, y) ]);
	editArrayElement(x, y, tmpAverage + offset);


InitGrid = InitGrid(7)
GenGrid(1.1);

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

vtxIndexList=[]
vtxWorldPosition = []    # will contain positions un space of all object vertex
def queryArrayElementVtxPos( shapeNode ) :
 	
 	global vtxIndexList
	vtxIndexList = cmds.getAttr( shapeNode+".vrts", multiIndices=True )
 
	for i in vtxIndexList :
		curPointPosition = cmds.xform( str(shapeNode)+".pnts["+str(i)+"]", query=True, translation=True, worldSpace=True )    # [1.1269192869360154, 4.5408735275268555, 1.3387055339628269]
		vtxWorldPosition.append( curPointPosition )
 
	return vtxWorldPosition


#precalculate random values
'''
size=5
randArray=[]
arraysize=size*size
for i in range(arraysize):
	randArray.append(random.random()*5)
print len(randArray)
'''

cmds.select(all=True)
cmds.delete()
p=cmds.polyPlane(width=10, height=10, subdivisionsX=size-1, subdivisionsY=size-1)
queryArrayElementVtxPos(p[0])

for i in range (0,len(vtxIndexList)):
		#y Vertex Coordinate	
		#print "vtxWorldPosition[i][2]=%s"%(vtxWorldPosition[i][2])
		
		vtxWorldPosition[i][1]=map[i] #randArray[i]
		
		#print "vtxWorldPosition[i][1]=%s"%(vtxWorldPosition[i][1]) 
		
		x,y,z=vtxWorldPosition[i]		
		#print "x=%f, y=%f, z=%f,"%(x,y,z)
		
		cmds.xform(p[0]+".vtx[%d]"%(i) , translation=[x,y/40,z], worldSpace=True)
		if (i % size) == 0:
			cmds.refresh()
		
		
		
		
		
		
		


