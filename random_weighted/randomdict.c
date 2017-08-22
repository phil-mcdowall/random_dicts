#include <Python.h>
#include <stdio.h>

//static char module_docstring[] =
//    "This module provides an interface for random weighted dictionary samples in C";
static char randomdict_docstring[] =
    "Draw a random sample from a dict, with size N, weighted by dictionary values";

static PyObject *randomdict_random_dict(PyObject *self, PyObject *args);

static PyMethodDef module_methods[] = {
{"random",randomdict_random_dict,METH_VARARGS,randomdict_docstring},
{NULL,NULL,0,NULL}
};

static struct PyModuleDef randomdict =
{
    PyModuleDef_HEAD_INIT,
    "randomdict", //name of module
    randomdict_docstring, //docstring
    -1, //?
    module_methods
};
int compare (const void * a, const void * b)
{
  float fa = *(const float*) a;
  float fb = *(const float*) b;
  return (fa > fb) - (fa < fb);
}

static PyObject *randomdict_random_dict(PyObject *self, PyObject *args)
{
    int N; //Number of draws
    float total; //sum of weights
    PyObject *dictionary; // Input dictionary
    PyObject *key, *value; // Key value pairs set during iteration
    Py_ssize_t pos = 0; // Counter for dictionary iteration

    // Template argument check (ags,Format string, memory addresses...)
     if(!PyArg_ParseTuple(args,"IOf",&N,&dictionary,&total))
        return NULL;

       if(total == 0.0){
//    float total = 0.0; // Var to store dictionary total
//    //Sum dictionary keys
    while (PyDict_Next(dictionary, &pos, &key, &value)) {
        total += PyFloat_AsDouble(value);
    };
}

    if(total == 0.0){
    return NULL;}

    //Generate N random floats between 0 and the sum of dictionary keys
    float targets[N];
    int i;
    for (i = 0; i < N; i++) {
    targets[i] = ((float)rand()/(float)RAND_MAX)*total;
    }

    //sort targets into ascending order
    qsort(targets,N,sizeof(float),compare);

    int target_ind = 0;
    float cum_total = 0.0;
    Py_ssize_t result_length = N; // length of results list
    PyObject* result_list = PyList_New(result_length); // results list
    //reset position counter to iterate dictionary again
    pos = 0;
    Py_ssize_t result_ind_py = 0;
    while (PyDict_Next(dictionary, &pos, &key, &value)) {
        cum_total += PyFloat_AsDouble(value);
        while((targets[target_ind] < cum_total) & (target_ind < N)){
            PyList_SetItem(result_list, result_ind_py, key);
            Py_INCREF(key);
            target_ind += 1;
            result_ind_py += 1;
        };
    };

return result_list;
};

PyMODINIT_FUNC PyInit_randomdict(void)
{
    return PyModule_Create(&randomdict);
}