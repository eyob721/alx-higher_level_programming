#include <stdio.h>
#include <string.h>

#include "Python.h"

/**
 * print_python_string - prints info on a python string object
 * @p: pointer to a PyObject
 *
 * Retrurn: void
 */
void print_python_string(PyObject *p)
{
	char *obj_type, *str_type, *value;
	ssize_t len, i = 0;
	int is_ascii;

	printf("[.] string object info\n");
	/* Check if the objects is a string object */
	obj_type = (char *)p->ob_type->tp_name;
	if (strcmp(obj_type, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	/* Determine type, length and value */
	is_ascii = PyUnicode_IS_ASCII(p);
	str_type = is_ascii ? "compact ascii" : "compact unicode object";
	len = PyUnicode_GET_LENGTH(p);
	value = (char *)PyUnicode_AsUTF8(p);

	printf("  type: %s\n", str_type);
	printf("  length: %ld\n", len);
	printf("  value: %s\n", value);
}
