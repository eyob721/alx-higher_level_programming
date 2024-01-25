#include <stdio.h>
#include <string.h>

#include "Python.h"

#define MAX_ASCII_HEX_SIZE 2
void ascii_hex(unsigned char ascii_char, char *buf);
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints info on a python list object
 * @p: pointer to a PyObject
 *
 * Retrurn: void
 */
void print_python_list(PyObject *p)
{
	PyListObject *l = (PyListObject *)p;
	ssize_t i, list_size;
	char *obj_type;

	printf("[*] Python list info\n");
	/* Check if the PyObject is a list type */
	obj_type = (char *)p->ob_type->tp_name;
	if (strcmp(obj_type, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	/* Print info on the list object */
	list_size = l->ob_base.ob_size;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", l->allocated);

	for (i = 0; i < list_size; ++i)
	{
		obj_type = (char *)l->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, obj_type);
		if (strcmp(obj_type, "bytes") == 0)
			print_python_bytes(l->ob_item[i]);
	}
}

/**
 * print_python_bytes - prints info on a python bytes object
 * @p: pointer to a PyObject
 *
 * Retrurn: void
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *b = (PyBytesObject *)p;
	ssize_t i, bytes_size, bytes_hex;
	char *obj_type, *str_value, hex_buf[MAX_ASCII_HEX_SIZE + 1] = {0};

	printf("[.] bytes object info\n");
	/* Check if the objects is a bytes object */
	obj_type = (char *)p->ob_type->tp_name;
	if (strcmp(obj_type, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Print bytes object info */
	bytes_size = b->ob_base.ob_size;
	str_value = b->ob_sval;
	bytes_hex = bytes_size + 1 <= 10 ? bytes_size + 1 : 10;

	printf("  size: %ld\n", bytes_size);
	printf("  trying string: %s\n", str_value);
	printf("  first %ld bytes: ", bytes_hex);

	for (i = 0; i < bytes_hex; ++i)
	{
		ascii_hex(str_value[i], hex_buf);
		printf("%s", hex_buf);
		if (i < bytes_hex - 1)
			printf(" ");
	}
	printf("\n");
}

/**
 * ascii_hex - converts a given ascii character in to hexadecimal, and writes
 *             it on a given buffer.
 * @ascii_char: ascii character to be converted
 * @buf: buffer to write it on
 *
 * Return: void
 */
void ascii_hex(unsigned char ascii_char, char *buf)
{
	char *hex = "0123456789abcdef";
	int rem = 0, i = MAX_ASCII_HEX_SIZE - 1;

	do
	{
		rem = ascii_char % 16;
		buf[i] = hex[rem];
		ascii_char /= 16;
	} while (--i >= 0);
}
