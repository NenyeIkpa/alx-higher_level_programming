#include "lists.h"

void delete_list(listint_t *h)
{
	listint_t *temp = NULL;

	while (h != NULL)
	{
		temp = h;
		h = h->next;
		free(temp);
	}
}

int is_palindrome(listint_t **head)
{
	listint_t *h = NULL, *node = NULL, *curr = NULL;

	if (head == NULL || *head == NULL)
	       return (1);
	curr = *head;
	while (curr != NULL)
	{
		node = malloc(sizeof(listint_t));
		if (node == NULL)
			return (0);
		node->n = curr->n;
		node->next = NULL;
		if (h == NULL)
			h = node;
		else
		{
			node->next = h;
			h = node;
		}
		curr = curr->next;
	}
	curr = *head;
	while ( curr != NULL && h != NULL)
	{
		if (curr->n != h->n)
		{
			delete_list(h);
			return (0);
		}
		curr = curr->next;
		h = h->next;
	}
	delete_list(h);
	return (1);
}	
