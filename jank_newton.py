import numpy as np

t=0
x0=40.
m=0.533
v0=-0.1
x=x0
vx=v0
vy=0.
dt=0.01
y0 =8.
y=y0


# while(True):

# 	kx1 = v
# 	kv1 = -m/(4.*x*x)

# 	kx2 = v + 0.5*dt*kv1
# 	kv2 = -m/(4.*(x + 0.5*dt*kx1)*(x + 0.5*dt*kx1))

# 	kx3 = v + 0.5*dt*kv2
# 	kv3 = -m/(4.*(x + 0.5*dt*kx2)*(x + 0.5*dt*kx2))

# 	kx4 = v + dt*kv3
# 	kv4 = -m/(4.*(x + dt*kx3)*(x + dt*kx3))

# 	x += dt*(kx1 + 2.*kx2 + 2.*kx3 + kx4)/6.
# 	v += dt*(kv1 + 2.*kv2 + 2.*kv3 + kv4)/6.
	
# 	t+= dt

# 	print("t = " + str(t) + ", x = " + str(x) )

# 	if (x < 0):
# 		break



while(True):

	r = np.sqrt(x*x + y*y) 
	kx1 = vx
	kvx1 = -m*x/(4.*r**3)
	ky1 = vy
	kvy1 = -m*y/(4.*r**3)

	r1 = np.sqrt((x + 0.5*dt*kx1)**2 + (y + 0.5*dt*ky1)**2)
	kx2 = vx + 0.5*dt*kvx1
	kvx2 = -m*(x+0.5*dt*kx1)/(4.*r1**3)
	ky2 = vy + 0.5*dt*kvy1
	kvy2 = -m*(y+0.5*dt*ky1)/(4.*r1**3)

	r2 = np.sqrt((x + 0.5*dt*kx2)**2 + (y + 0.5*dt*ky2)**2)
	kx3 = vx + 0.5*dt*kvx2
	kvx3 = -m*(x+0.5*dt*kx2)/(4.*r2**3)
	ky3 = vy + 0.5*dt*kvy2
	kvy3 = -m*(y+0.5*dt*ky2)/(4.*r2**3)

	r3 = np.sqrt((x + dt*kx3)**2 + (y + dt*ky3)**2)
	kx4 = vx + dt*kvx3
	kvx4 = -m*(x+dt*kx3)/(4.*r3**3)
	ky4 = vy + dt*kvy3
	kvy4 = -m*(y+dt*ky3)/(4.*r3**3)

	x += dt*(kx1 + 2.*kx2 + 2.*kx3 + kx4)/6.
	vx += dt*(kvx1 + 2.*kvx2 + 2.*kvx3 + kvx4)/6.
	y += dt*(ky1 + 2.*ky2 + 2.*ky3 + ky4)/6.
	vy += dt*(kvy1 + 2.*kvy2 + 2.*kvy3 + kvy4)/6.
	
	t+= dt

	print("t = " + str(t) + ", x = " + str(x) + ", y = " + str(y) + ", r = " + str(r) )

	if (r < 10.):
		dt = r/1000.
	if (np.sqrt(x*x + y*y)>r):
		break