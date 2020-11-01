import math
AB,BC=int(input()),int(input())
hype=math.hypot(AB,BC)                      #to calculate hypotenuse
res=round(math.degrees(math.acos(BC/hype))) #to calculate required angle 
degree=chr(176)                                #for DEGREE symbol
print(res,degree, sep='')
