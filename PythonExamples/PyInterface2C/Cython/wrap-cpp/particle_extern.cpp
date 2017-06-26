#include "particle_extern.h"

Particle::Particle(float m, float c, float *p, float *v) :
    mass(m), charge(c) 
{
    for (int i=0; i<3; ++i) {
        pos[i] = p[i]; vel[i] = v[i];
    }
}

void Particle::applyImpulse(float *f, float t)
{
    float newvi;
    for(int i=0; i<3; ++i) {
        newvi = vel[i] + t / mass * f[i];
        pos[i] = (newvi + vel[i]) * t / 2.;
        vel[i] = newvi;
    }
}
