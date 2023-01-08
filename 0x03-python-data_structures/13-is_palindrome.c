#include "lists.h"
#define LINKED_LIST_PTR_ARRAY_SIZE 100

/**
 * llen - returns the length or size of the linked list
 * @head: target linked list
 * Return: size/length
 */
int llen(listint_t *head)
{
	int size = 0;
	listint_t *current;

	if (head == NULL)
		return (size);

	current = head;
	while (current != NULL)
	{
		current = current->next;
		size++;
	}
	return (size);
}

/**
 * is_palindrome - this function check if a linked lis is a palindrome
 * @head: pointer to the head node pointer
 * Return: 1 if true, 0 if false
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i;
	listint_t *arr[LINKED_LIST_PTR_ARRAY_SIZE];
	listint_t *current;

	if (head == NULL || (*head) == NULL)
		return (0);

	current = (*head);

	for (i = 0; current != NULL; i++, len++)
	{
		arr[i] = current;
		current = current->next;
	}

	for (i = 0; i < len / 2; i++)
	{
		if (arr[i]->n != arr[(len - 1) - i]->n)
			return (0);
	}
	return (1);
}
