#include "main.h"

/**
 * print_python_list_info - This function print the info about the
 * size of a python list, the memory allocated,
 * and the types of all the element in a python list
 * @p: python list PyObject
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
	int i;
	Py_ssize_t list_size = PyList_Size(p);
	PyListObject *vobj = (PyListObject *)p;
	PyObject *item;

	printf("[*] Size of the Python List = %d\n", (int)list_size);
	printf("[*] Allocated = %d\n", (int)vobj->allocated);

	for (i = 0; i < (int)list_size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
	}
}
