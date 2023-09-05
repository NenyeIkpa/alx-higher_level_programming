#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *current, *tortoise, *hare;

	if (list == NULL)
		return (0);
	current = list;
	tortoise = list;
	hare = list;
	while (current->next->next!= NULL)
	{
		tortoise = current->next;
		hare = current->next->next;
		if (hare == tortoise)
			return (1);
		current = current->next;
	}
	return (0);
}
