void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyListObject pyobj;

	size = (int) PyList_Size(p);
	alloc = (int) ((PyListObject *) p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	
	for (i = 0; i < size; i++)
	{
		pyobj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(pyobj)->tp_name);
	}
}
