#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/queue.h"

Queue* queue_create(void) {
    Queue *q = malloc(sizeof(Queue));
    if (!q) return NULL;
    q->front = q->rear = NULL;
    q->size  = 0;
    return q;
}

int queue_is_empty(Queue *q) {
    return q ? (q->front == NULL) : 1;
}

void queue_enqueue(Queue *q, Order o) {
    if (!q) return;
    QNode *node = malloc(sizeof(QNode));
    if (!node) { perror("malloc"); return; }
    node->data = o;
    node->next = NULL;

    if (queue_is_empty(q)) {
        q->front = q->rear = node;
    } else {
        q->rear->next = node;
        q->rear       = node;
    }
    q->size++;
}

Order queue_dequeue(Queue *q) {
    Order invalid = {-1, 0, "", ""};
    if (!q || queue_is_empty(q)) return invalid;

    QNode *tmp = q->front;
    Order  o   = tmp->data;
    q->front   = q->front->next;
    if (q->front == NULL) q->rear = NULL;
    free(tmp);
    q->size--;
    return o;
}

void queue_destroy(Queue *q) {
    if (!q) return;
    while (!queue_is_empty(q))
        queue_dequeue(q);
    free(q);
}