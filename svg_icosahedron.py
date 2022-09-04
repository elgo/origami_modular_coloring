import drawSvg as draw
import math

dsize = 600
ang3 = 2*math.pi/3
ang6 = math.pi/3
d = draw.Drawing(dsize, dsize, origin='center', displayInline=False)
polar2xy = lambda r,the: (r*math.cos(the),r*math.sin(the))
mulvec = lambda f,v: [f*val for val in v]
addvec = lambda v1,v2: [v1[i]+v2[i] for i in range(0,2)]
points1 = [polar2xy(100,ang3*i) for i in range(0,3)]
points1+= [polar2xy(200,ang3*(i+0.5)) for i in range(0,3)]
points1+= [polar2xy(250,ang3*i) for i in range(0,3)]
points1+= [polar2xy(300,ang3*(i+0.5)) for i in range(0,3)]
#print(points1)
refline = [
        (0,1),(1,2),(2,0),
        (0,3),(0,5),(1,4),(1,3),(2,5),(2,4),
        (5,6),(0,6),(3,6), (3,7),(1,7),(4,7), (4,8),(2,8),(5,8),
        (6,9),(3,9),(7,9), (7,10),(4,10),(8,10), (8,11),(5,11),(6,11),
]
for r in refline:
        d.append(draw.Lines(*points1[r[0]],*points1[r[1]],stroke='black'))
for i in range(0,3):
        p1,p2 = points1[9+i], points1[9+((i+1)%3)]
        p = draw.Path(stroke='black',fill='none')
        vecn = mulvec(1.15,addvec(p1,p2))
        p.M(*p1)
        p.C(*vecn,*vecn,*p2)
        d.append(p)

d.saveSvg('result.svg')