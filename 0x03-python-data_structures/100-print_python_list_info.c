#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists.
 *
 * @p: PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyListObject *pylist, *pyobj;

	size = (int) PyList_Size(p);
	alloc = (int) ((PyListObject *) p)->allocated;
	pylist = (PyListObject *) p;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	
	for (i = 0; i < size; i++)
	{
		pyobj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(pyobj)->tp_name);
	}
}
