#include "lists.h"

/**
 * insert_node - insert node to a sorted linked list
 * @head: pointer to head node pointer
 * @number: value of the new node
 * Return: NULL on failure or address of new node on success
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp, *new_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		(*head) = new_node;
		return (new_node);
	}
	if ((*head)->n > number)
	{
		temp = (*head)->next ? (*head)->next : NULL;
		(*head) = new_node;
		new_node->n = temp;
		return (new_node);
	}
	for (node = (*head); node != NULL; node = node->next)
	{
		if (node->next == NULL)
		{
			node->next = new_node;
			return (new_node);
		}

		if (node->next->n > number)
		{
			temp = node->next;
			node->next = new_node;
			new_node->next = temp;
			return (new_node);
		}
	}
	return (NULL);
}
