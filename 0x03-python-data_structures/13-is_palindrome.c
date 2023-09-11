#include "lists.h"

/**
 * is_palindrome - a function that checks if a singly linked list is a
 *                 palindrome.
 * @head: double pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int data_front, data_back, list_size, i, j;

	if (head == NULL)
		return (0);
	list_size = get_list_size(*head);
	for (i = 0, j = list_size - 1; i <= j; ++i, --j)
	{
		data_front = get_data_at_index(*head, i);
		data_back = get_data_at_index(*head, j);
		if (data_front != data_back)
			return (0);
	}
	return (1);
}

/**
 * get_data_at_index - a function that fetchs the data of a node at a given
 *                     index in the list
 * @head: pointer to the head of the list
 * @idx: index of the node to fetch data from
 *
 * Return: data of the node at a given index
 */
int get_data_at_index(listint_t *head, int idx)
{
	int i = 0;

	while (i++ < idx && head != NULL)
		head = head->next;
	return (head->n);
}

/**
 * get_list_size - a function that computes the size of the list
 * @head: pointer to the head of the list
 *
 * Return: size of the list
 */
int get_list_size(listint_t *head)
{
	int list_size = 0;

	while (head != NULL)
	{
		head = head->next;
		++list_size;
	}
	return (list_size);
}
