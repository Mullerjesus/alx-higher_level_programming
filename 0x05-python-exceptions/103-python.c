#include <python.h>
#include <stdio.h>

/**
* print_python_list - Prints some basic info about Python lists.
* @p: A PyObject list object.
*/
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *obj;

if (!PyList_Check(p))
{
fprintf(stderr, "[ERROR] Invalid List Object\n");
return;
}

size = PyList_Size(p);
printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
obj = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
if (PyBytes_Check(obj))
print_python_bytes(obj);
}
}

/**
* print_python_bytes - Prints some basic info about Python bytes objects.
* @p: A PyObject bytes object.
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;

if (!PyBytes_Check(p))
{
fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
str = PyBytes_AsString(p);
printf("[.] bytes object info\n  size: %ld\n  trying string: %s\n  first 10 bytes: ", size, str);
for (i = 0; i < size && i < 10; i++)
{
printf("%02x ", (unsigned char)str[i]);
}
printf("\n");
}
