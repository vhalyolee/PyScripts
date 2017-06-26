#ifndef _PARTICLE_EXTERN_H_
#define _PARTICLE_EXTERN_H_

class Particle {

    public:

        Particle() :
            mass(0), charge(0) {}
        
        Particle(float m, float c, float *p, float *v);

        ~Particle() {}

        float getMass() {return mass; }

        void setMass(float m) { mass = m; }

        float getCharge() { return charge; }

        const float *getVel() { return vel; }
        const float *getPos() { return pos; }

        void applyImpulse(float *f, float t);

    private:
        float mass, charge;
        float pos[3], vel[3];
};

#endif
