
#include<stdio.h>
#include<stdlib.h>

struct node
{
  int data;
  struct node *next;
};

int main(){
    struct node *head;
    struct node *one = NULL;
    struct node *two = NULL;
    struct node *three = NULL;

    /* Allocate memory */
    one = malloc(sizeof(struct node));
    two = malloc(sizeof(struct node));
    three = malloc(sizeof(struct node));

    /* Assign data values */
    one->data = 100;
    two->data = 2;
    three->data=3;

    /* Connect nodes */
    one->next = two;
    two->next = three;
    three->next = NULL;

    printf("%d\n",one->data);
    printf("%d",two->data);
}