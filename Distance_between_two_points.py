import math
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
distance=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
#distance=math.sqrt((15-25)**2+(10-35)**2)
print("{:.4f}".format(distance))