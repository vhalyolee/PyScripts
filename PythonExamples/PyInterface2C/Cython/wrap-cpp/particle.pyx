import numpy as np

cdef extern from "particle_extern.h":

    cppclass _Particle "Particle":
        _Particle(float m, float c, float *p, float *v)
        float getMass()
        void setMass(float m)
        float getCharge()
        const float *getVel()
        const float *getPos()
        void applyImpulse(float *f, float t)


cdef class Particle:
    cdef _Particle *thisptr # ptr to C++ instance

    def __cinit__(self, m, c, float[::1] p, float[::1] v):
        if p.shape[0] != 3 or v.shape[0] != 3:
            raise ValueError("...")
        self.thisptr = new _Particle(m, c, &p[0], &v[0])

    def __dealloc__(self):
        del self.thisptr

    def apply_impulse(self, float[::1] v, float t):
        self.thisptr.applyImpulse(&v[0], t)

    def __repr__(self):
        args = ', '.join('%s=%s' % (n, getattr(self, n)) for n in ('mass', 'charge', 'pos', 'vel'))
        return 'particle.Particle(%s)' % args

    property charge:

        def __get__(self):
            return self.thisptr.getCharge()

    property mass:  # Cython-style properties.

      def __get__(self):
        return self.thisptr.getMass()

      def __set__(self, m):
        self.thisptr.setMass(m)

    property vel:

        def __get__(self):
            cdef const float *_vel = self.thisptr.getVel()
            cdef float[::1] arr = np.empty((3,), dtype=np.float32)
            for i in range(3):
                arr[i] = _vel[i]
            return np.asarray(arr)

    property pos:

        def __get__(self):
            cdef const float *_pos = self.thisptr.getPos()
            cdef float[::1] arr = np.empty((3,), dtype=np.float32)
            for i in range(3):
                arr[i] = _pos[i]
            return np.asarray(arr)
