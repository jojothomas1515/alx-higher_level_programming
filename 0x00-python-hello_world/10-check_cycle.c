#include "lists.h"

/**
 * check_cycle - checks if the singly linked list has a cycle in it
 * @list: linked list
 * Return: 0
 */

int check_cycle(listint_t *list)
{
	listint_t *n, *t;

	if (list == NULL)
		return (0);

	n = list;
	t = list->next;

	for (; n && t; t = t->next, n = n->next->next)
	{
		if (n == n->next)
			return (1);
		if (n == t)
			return (1);
		if (n == t->next)
			return (1);
	}
	return (0);
}
