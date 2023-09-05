#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = list;
	hare = list;
	while (hare != NULL && hare->next!= NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (hare == tortoise)
			return (1);
	}
	return (0);
}
