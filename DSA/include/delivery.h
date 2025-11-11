#ifndef DELIVERY_H
#define DELIVERY_H

#include "queue.h"
#include "bst.h"

typedef struct Platform {
    Queue *pending;     /* orders waiting for prep */
    Queue *ready;       /* orders prepared, awaiting agent */
    BST   *in_transit;  /* active deliveries */
    int    next_order_id;
    int    next_agent_id;
} Platform;

/* API (exactly the functions asked for) */
Platform* init_platform(void);
void      place_order(Platform *p, const char *rest, const char *cust, int prep_mins);
void      prepareOrder(Platform *p);
void      assignDeliveryAgent(Platform *p);
void      trackOrder(Platform *p, int order_id);
void      generateReport(Platform *p);
void      destroy_platform(Platform *p);

#endif