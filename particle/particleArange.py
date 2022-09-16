import math
import numpy as np

dp=1000e-9

R=12.6e-3*0.5
R2=R*R
z=-1e-3

with open("particleSet","w") as f:
	f.write("x\ty\tz\tdp\n")
	for x in np.arange(-R, R, 1e-3):
		for y in np.arange(-R, R, 1e-3):
			r2=x*x+y*y
			if(r2<R2):
				f.write(str(x)+"\t"+str(y)+"\t"+str(z)+"\t"+str(dp)+"\n")
		
