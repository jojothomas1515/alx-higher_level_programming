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
	t_node = list->next;
	while (n_node && t_node->next)
	{

		if (n_node == n_node->next || n_node == n_node->next->next)
			return (1);

		if (n_node == t_node || n_node == t_node->next)
			return (1);

		n_node = n_node->next;
		t_node = t_node->next->next;
	}
	return (0);
}
