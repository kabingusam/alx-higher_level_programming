/**
 * Author : Kabingu Sammy.
 *
 */
 #include <stdlib.h>
 #include "lists.h"

 /**
  * check_cycle : checks wether a linked list is cyclic.
  * 
  * return 0 : if list is not cyclic.
  * return 1 : if list is cyclic.
  */
int check_cycle(listint_t *list)
{
    listint_t *kabi, *sami;
    
    if(list == NULL || list->next == NULL)
        return(0);
    
    kabi = kabi->next;
    sami = kabi->next->next;

    while(kabi && sami && sami->next)
    {
        if(kabi = sami)
            return(1);
        kabi = kabi->next;
        sami = kabi->next->next;
    }
    return(0);
}