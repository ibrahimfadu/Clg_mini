#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "../include/delivery.h"

// Number Generator
static int rand_range(int min, int max) {
    return min + rand() % (max - min + 1);
}


/* ---------- Platform ---------- */
Platform* init_platform(void) {
    Platform *p = malloc(sizeof(Platform));
    if (!p) return NULL;
    p->pending    = queue_create();
    p->ready      = queue_create();
    p->in_transit = bst_create();
    p->next_order_id = 1000;
    p->next_agent_id = 1; 
    srand((unsigned)time(NULL));
    return p;
}

/* ---- place_order ---- */
void place_order(Platform *p, const char *rest, const char *cust, int prep_mins){
    if (!p || !p->pending) return;
    Order o = {0};
    o.order_id = p->next_order_id++;
    o.prep_time = prep_mins > 0 ? prep_mins : 1;
    strncpy(o.restaurant, rest, 31);
    strncpy(o.customer,   cust, 31);
    queue_enqueue(p->pending, o);
    printf("Order %d placed (%s → %s, prep=%d min)\n",
           o.order_id, o.restaurant, o.customer, o.prep_time);
}

/* ---- prepareOrder ---- */
void prepareOrder(Platform *p) {
    if (!p || queue_is_empty(p->pending)) {
        printf("No orders to prepare.\n");
        return;
    }
    Order o = queue_dequeue(p->pending);
    /* Simulate preparation time */
    printf("Preparing order %d... (%d min)\n", o.order_id, o.prep_time); /* In a real system you would sleep(o.prep_time*60) */
    queue_enqueue(p->ready, o);
    printf("Order %d is READY for delivery.\n", o.order_id);
}

/* ---- assignDeliveryAgent ---- */
void assignDeliveryAgent(Platform *p) {
    if (!p || queue_is_empty(p->ready)) {
        printf("No ready orders to assign.\n");
        return;
    }
    Order o = queue_dequeue(p->ready);
    int agent = p->next_agent_id++;
    int eta   = rand_range(10, 45);   /* random ETA */

    Delivery d = {o.order_id, agent, eta, "en-route"};
    if (bst_insert(p->in_transit, d)) {
        printf("Agent %d assigned to order %d (ETA %d min)\n",
               agent, o.order_id, eta);
    }
}

/* ---- trackOrder ---- */
void trackOrder(Platform *p, int order_id) {
    if (!p) return;
    /* 1) check ready queue */
    int found = 0;
    QNode *cur = p->ready ? p->ready->front : NULL;
    while (cur) {
        if (cur->data.order_id == order_id) {
            printf("Order %d is READY (awaiting agent).\n", order_id);
            found = 1; break;
        }
        cur = cur->next;
    }
    if (found) return;

    /* 2) check in-transit BST */
    BSTNode *n = bst_search(p->in_transit, order_id);
    if (n) {
        printf("Order %d: Agent %d, %s, ETA %d min\n",
               n->data.order_id, n->data.agent_id,
               n->data.status, n->data.eta);
        return;
    }
    printf("Order %d not found.\n", order_id);
}

/* ---- generateReport ---- */
static void _print_delivery(Delivery d) {
    printf("  Order %d | Agent %d | ETA %d min | %s\n",
           d.order_id, d.agent_id, d.eta, d.status);
}
void generateReport(Platform *p) {
    if (!p) return;
    printf("\n=== PLATFORM REPORT ===\n");
    printf("Pending orders : %d\n", p->pending ? p->pending->size : 0);
    printf("Ready orders   : %d\n", p->ready   ? p->ready->size   : 0);
    printf("In transit     : %s\n", p->in_transit && p->in_transit->root ?
                                 "see below" : "none");
    if (p->in_transit && p->in_transit->root) {
        printf("Deliveries (sorted by ETA):\n");
        bst_inorder(p->in_transit, _print_delivery);
    }
    printf("========================\n\n");
}

/* ---- cleanup ---- */
void destroy_platform(Platform *p) {
    if (!p) return;
    queue_destroy(p->pending);
    queue_destroy(p->ready);
    bst_destroy(p->in_transit);
    free(p);
}
