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
	listint_t *tmp_head;

	if (head == NULL)
		return (0);
	tmp_head = *head;
	return (check_palindrome(&tmp_head, *head));
}

/**
 * check_palindrome - a function that checks if a singly linked list is a
 *                    palindrome using recursion.
 * @left: double pointer to a node on the left side
 * @right: pointer to a node on the right side
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int check_palindrome(listint_t **left, listint_t *right)
{
	int is_palindrome = 0;

	if (right == NULL)
		return (1);
	is_palindrome = check_palindrome(left, right->next);
	if (is_palindrome != 0)
	{
		is_palindrome = (*left)->n == right->n;
		*left = (*left)->next;
	}
	return (is_palindrome);
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
