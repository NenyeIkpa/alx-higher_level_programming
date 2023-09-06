#include "lists.h"

/**
 * insert_node - inserts a new node to a sorted list
 *
 * @head: head pointer
 * @number: new node to be inserted
 *
 * Return: address of the new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *prev, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (head == NULL || *head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	curr = *head;
	while (curr != NULL)
	{
		if (curr->n < number)
		{
			prev = curr;
			curr = curr->next;
		}
		else
		{
			new_node->next = prev->next;
			prev->next = new_node;
			break;
		}
	}
	return (new_node);
}
