#include <stdlib.h>
#include <stdio.h>
#include "food_delivery.h"
//assignDeliveryAgent(),
//prepareOrder(),
//trackOrder(),
//generateReport()

node* createNode(int data){
  node* newNode=malloc(sizeof(node));
  newNode->data=data;
  newNode->link=NULL;
  return newNode;
}


void init(queue *queue){
    queue->rear=NULL;
   queue->front=NULL;
}

void enqueue(queue* queue,int data){ 
  node* newNode=createNode(data);
  if(queue->front==NULL){
    queue->front=newNode;
    queue->rear=newNode;
  }else{ 
  queue->rear->link=newNode;
  queue->rear=newNode;
  }
}
int dequeue(queue* queue){
  node* temp=queue->front;
  int delval=queue->front->data;
  queue->front=queue->front->link;
  free(temp);
  return delval;
}

void display(queue* queue){
  node* temp=queue->front;
  while(temp!=queue->rear){
    printf("%d ->",temp->data);
    temp=temp->link;
  }
  printf("%d",temp->data);

}



