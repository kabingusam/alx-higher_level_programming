#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h); //for the file linked_list.c
listint_t *add_nodeint_end(listint_t **head, const int n); //for the file linked_list.c
void free_listint(listint_t *head); //for the file linked_list.c

listint_t *insert_node(listint_t **head, int number);//for the file 13-insert_number.c

#endif /* LISTS_H */