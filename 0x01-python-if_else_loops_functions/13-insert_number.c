#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"
/**
 * Return: the address of the new node, or NULL if it failed
 * function to inserts a number into a sorted singly linked list
 * @n : integer to be included in the new node
 * @head : head of the linked list.
 * @new : the new node to be inserted.
 * @next : points to the next node.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = *head , *new;

    new = malloc(sizeof(listint_t));
    if(new == NULL)
        return(NULL);
    new->n = number;
    if(node == NULL || node-> >= number)
    {
        new->next = node;
        *head = new;
        return(new);

    }

   

}

// algorithim
//  0. If node to be inserted is null return null.
//  1. If Linked list is empty then make the node as head and return it.
//  2. If the value of the node to be inserted is smaller than the value of the head node, then insert the node 
//     at the start and make it head.
