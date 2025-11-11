#ifndef BST_H
#define BST_H

typedef struct Delivery {
    int   order_id;
    int   agent_id;
    int   eta;            /* minutes from now */
    char  status[16];     /* "en-route", "delivered" */
} Delivery;

typedef struct BSTNode {
    Delivery          data;
    struct BSTNode   *left;
    struct BSTNode   *right;
} BSTNode;

typedef struct BST {
    BSTNode *root;
} BST;

/* API */
BST*    bst_create(void);
BSTNode* bst_insert(BST *t, Delivery d);
BSTNode* bst_search(BST *t, int order_id);
BSTNode* bst_min_node(BSTNode *n);
void    bst_delete(BST *t, int order_id);
void    bst_inorder(BST *t, void (*visit)(Delivery));
void    bst_destroy(BST *t);

#endif