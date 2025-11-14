#ifndef QUEUE_H
#define QUEUE_H

typedef struct Order {
    int   order_id;
    int   prep_time;      /* minutes */
    char  restaurant[32];
    char  customer[32];
} Order;

typedef struct QNode {
    Order        data;
    struct QNode *next;
} QNode;

typedef struct Queue {
    QNode *front;
    QNode *rear;
    int    size;
} Queue;



Queue*  queue_create(void);
int     queue_is_empty(Queue *q);
void    queue_enqueue(Queue *q, Order o);
Order   queue_dequeue(Queue *q);
void    queue_destroy(Queue *q);

#endif
