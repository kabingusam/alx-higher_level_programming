#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *kabi, *sami;

	if (list == NULL || list->next == NULL)
		return (0);

	kabi = list->next;
	sami = list->next->next;

	while (kabi && sami && sami->next)
	{
		if (kabi == sami)
			return (1);

		kabi = kabi->next;
		sami = sami->next->next;
	}

	return (0);
}
