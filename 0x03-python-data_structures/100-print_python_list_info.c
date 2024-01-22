#include "Python.h"
#include "lists.h"

/**
 * print_python_list_info - a function that prints some basic info about a
 *                          given Python list
 * @p: pointer to PyObject
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list_obj = (PyListObject *)p;
	int i = 0;
	ssize_t list_size, list_allocated;
	char *list_item_type;

	list_size = PyList_Size(p);
	list_allocated = list_obj->allocated;
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list_allocated);
	for (i = 0; i < list_size; ++i)
	{
		list_item_type = (char *)Py_TYPE(list_obj->ob_item[i])->tp_name;
		printf("Element %d: %s\n", i, list_item_type);
	}
}
