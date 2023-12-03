#include "lists.h"
#include <stddef.h>

/**
* reverse_list - Reverses a linked list.
* @head: Pointer to the head of the linked list.
*/
void reverse_list(listint_t **head);

/**
* compare_lists - Compares two linked lists.
* @list1: Pointer to the head of the first linked list.
* @list2: Pointer to the head of the second linked list.
*
* Return: 1 if the lists are the same, 0 otherwise.
*/
int compare_lists(listint_t *list1, listint_t *list2);

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: Pointer to the head of the linked list.
*
* Return: 1 if it is a palindrome, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{
listint_t *slow_ptr = *head, *fast_ptr = *head;
listint_t *prev_slow = *head;
listint_t *second_half, *mid_node = NULL;
int is_palindrome = 1;

if (*head != NULL && (*head)->next != NULL)
{
/* Use two pointers to find the middle of the linked list */
while (fast_ptr != NULL && fast_ptr->next != NULL)
{
fast_ptr = fast_ptr->next->next;
prev_slow = slow_ptr;
slow_ptr = slow_ptr->next;
}

/* If the number of elements is odd, move to the next element */
if (fast_ptr != NULL)
{
mid_node = slow_ptr;
slow_ptr = slow_ptr->next;
}

/* Reverse the second half of the linked list */
reverse_list(&slow_ptr);

/* Compare the first half and the reversed second half */
is_palindrome = compare_lists(*head, slow_ptr);

/* Reconstruct the original linked list */
reverse_list(&slow_ptr);
if (mid_node != NULL)
{
prev_slow->next = mid_node;
mid_node->next = slow_ptr;
}
else
{
prev_slow->next = slow_ptr;
}
}

return (is_palindrome);
}
