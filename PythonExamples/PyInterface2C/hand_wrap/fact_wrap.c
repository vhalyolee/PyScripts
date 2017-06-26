#include "Python.h"
#include "fact.h"

/* define the wrapper functions exposed to Python (must be statis) */

static PyObject* wrap_fact(PyObject *self, PyObject *args) 
{
    int n, result;
    /* Python->C Conversion */
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;
    
    /* Call our function */
    result = fact(n);
    
    /* C->Python Conversion */
    return Py_BuildValue("i", result);
}

/* Method table decalaring the names of functions exposed to Python */

static PyMethodDef ExampleMethods[] = {
    {"fact",  wrap_fact, METH_VARARGS, "Calculate the factorial of n"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

/* Moudule initialization functioncalled the "import example */

PyMODINIT_FUNC
initexample(void)
{
    (void) Py_InitModule("example", ExampleMethods);
}
