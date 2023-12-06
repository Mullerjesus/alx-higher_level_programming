#include <stdio.h>

void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyListObject *list = (PyListObject *)p;

size = PyList_Size(p);
printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, list->allocated);
for (i = 0; i < size; i++)
{
printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
if (PyBytes_Check(PyList_GetItem(p, i)))
print_python_bytes(PyList_GetItem(p, i));
}
}

void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
PyBytesObject *bytes = (PyBytesObject *)p;

printf("[.] bytes object info\n");
if (PyBytes_Check(p))
{
size = PyBytes_Size(p);
printf("  size: %ld\n", size);
printf("  trying string: %s\n", PyBytes_AS_STRING(p));
printf("  first %ld bytes: ", size < 10 ? size : 10);
for (i = 0; i < size && i < 10; i++)
{
printf("%02x", (unsigned char)bytes->ob_sval[i]);
if (i < size - 1 && i < 9)
printf(" ");
}
printf("\n");
}
else
{
printf("  [ERROR] Invalid Bytes Object\n");
}
}
