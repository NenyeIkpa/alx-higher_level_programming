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
	listint_t *h = NULL, *node = NULL, *next = NULL, *prev = NULL;

	if (head == NULL || *head == NULL)
	       return (1);
	node = *head;
	while (node)
	{		
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	h = prev;
	while ( *head != NULL && h != NULL)
	{
		if ((*head)->n != h->n)
		{
			delete_list(h);
			return (0);
		}
		*head = (*head)->next;
		h = h->next;
	}
	delete_list(h);
	return (1);
}	
