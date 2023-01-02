#include "lists.h"

/**
 * check_cycle - checks if the singly linked list has a cycle in it
 * @list: linked list
 * Return: 0
 */

int check_cycle(listint_t *list)
{
	listint_t *n_node, *t_node;

	if (list == NULL)
		return (0);

	n_node = list;
	while (n_node)
	{
		t_node = list;

		if (n_node == n_node->next)
			return (1);

		while (t_node != n_node)
		{
			if (t_node == n_node->next)
				return (1);
			t_node = t_node->next;
		}
		n_node = n_node->next;
	}
	return (0);
}
