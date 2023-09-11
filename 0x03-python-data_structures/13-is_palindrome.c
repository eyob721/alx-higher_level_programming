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
	int data_front, data_back, list_size, i, j, mid_idx;
	listint_t *mid_node;

	if (head == NULL)
		return (0);
	list_size = get_list_size(*head);
	mid_idx = ((list_size - 1) / 2) + ((list_size - 1) % 2);
	mid_node = get_node_at_index(*head, mid_idx);
	for (i = 0, j = list_size - 1; i <= j; ++i, --j)
	{
		data_front = get_node_at_index(*head, i)->n;
		data_back = get_node_at_index(mid_node, j - mid_idx)->n;
		if (data_front != data_back)
			return (0);
	}
	return (1);
}

/**
 * get_node_at_index - a function that fetches the data of a node at a given
 *                     index in the list
 * @head: pointer to the head of the list
 * @idx: index of the node to fetch data from
 *
 * Return: data of the node at a given index
 */
listint_t *get_node_at_index(listint_t *head, int idx)
{
	int i = 0;

	while (i++ < idx && head != NULL)
		head = head->next;
	return (head);
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
