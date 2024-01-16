#include "lists.h"

/**
 * insert_node - a function that inserts a number into a sorted linked list
 * @head: double pointer to the head of the list
 * @number: number to be inserted
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *cur, *prev;

	if (head == NULL)
		return (NULL);
	/* Create the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	/* Find the correct place to put it */
	prev = cur = *head;
	while (cur != NULL && cur->n < number)
	{
		prev = cur;
		cur = cur->next;
	}
	/* Place the new node in the list */
	new_node->next = cur;
	if (cur == *head)
		*head = new_node;
	else
		prev->next = new_node;
	return (new_node);
}
