import particle
import numpy as np

pos = vel = np.arange(3., dtype=np.float32)
mass = 1.0
charge = 3.0

p = particle.Particle(mass, charge, pos, vel)

force = np.empty_like(vel)
force.fill(10.0)
time = 1.0

print "p before impulse: ", p
p.apply_impulse(force, time)
print "p after impulse : ", p
