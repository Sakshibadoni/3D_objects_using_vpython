# import the module
from vpython import * 
arrow(color = vector(5, 1, 0), 
      opacity = 0.5, 
      shininess = 1, 
      emissive = False)

arrow(pos = vector(-3, 1, 0),
      shaftwidth = 1,
      headwidth = 1,
      headlength = 2,
      color = vector(1, 1, 0))

arrow(pos = vector(-7, -2, 0),
	color = vector(1, 0, 1),
	axis = vector(1, 2, 2),
	up = vector(-1, 5, 2))

mybox = box(pos=vector(5, 0, 0),             
            size=vector(2,3,1) )

spring = helix(pos=vector(-4,-2,1),
               color = vector(1, 3, 2),
            axis=vector(5,0,0), radius=0.5)

ball = sphere(pos=vector(-1,2,1),
                radius=0.5)

handle = cylinder( size=vector(1,.2,.2),                   
                   color=vector(0.72,0.42,0) )

head = box( size=vector(.2,.6,.2), pos=vector(1.1,0,0),              ccolor=color.gray(.6) )

hammer = compound([handle, head])
hammer.axis = vector(1,1,0)
hammer.pos = vector(-6,1,0)

rod = cylinder(pos=vector(0,4,1),  
               axis=vector(1,1,1),
               color = vector(0,0,1), radius=1)

ring(pos=vector(-0.5,5.5,1),
        axis=vector(1,1,6),
        color = vector(0,0,1),
        radius=0.5, thickness=0.1)
