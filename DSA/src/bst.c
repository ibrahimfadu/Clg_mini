#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/bst.h"

static BSTNode* _new_node(Delivery d) {
    BSTNode *n = malloc(sizeof(BSTNode));
    if (!n) return NULL;
    n->data = d;
    n->left = n->right = NULL;
    return n;
}

BST* bst_create(void) {
    BST *t = malloc(sizeof(BST));
    if (t) t->root = NULL;
    return t;
}

BSTNode* bst_insert(BST *t, Delivery d) {
    if (!t) return NULL;
    BSTNode **cur = &t->root;
    while (*cur) {
        if (d.eta < (*cur)->data.eta)
            cur = &(*cur)->left;
        else
            cur = &(*cur)->right;
    }
    *cur = _new_node(d);
    return *cur;
}

BSTNode* bst_search(BST *t, int order_id) {
    if (!t) return NULL;
    BSTNode *cur = t->root;
    while (cur) {
        if (order_id == cur->data.order_id) return cur;
        if (order_id < cur->data.order_id)
            cur = cur->left;
        else
            cur = cur->right;
    }
    return NULL;
}

BSTNode* bst_min_node(BSTNode *n) {
    while (n && n->left) n = n->left;
    return n;
}

/* Delete by copying successor (standard BST delete) */
static BSTNode* _delete(BSTNode *root, int order_id) {
    if (!root) return NULL;
    if (order_id < root->data.order_id)
        root->left = _delete(root->left, order_id);
    else if (order_id > root->data.order_id)
        root->right = _delete(root->right, order_id);
    else {
        if (!root->left) { BSTNode *tmp = root->right; free(root); return tmp; }
        if (!root->right){ BSTNode *tmp = root->left;  free(root); return tmp; }
        BSTNode *succ = bst_min_node(root->right);
        root->data = succ->data;
        root->right = _delete(root->right, succ->data.order_id);
    }
    return root;
}
void bst_delete(BST *t, int order_id) {
    if (t) t->root = _delete(t->root, order_id);
}

/* In-order walk → earliest ETA first */
void bst_inorder(BST *t, void (*visit)(Delivery)) {
    if (!t || !visit) return;
    void _walk(BSTNode *n) {
        if (!n) return;
        _walk(n->left);
        visit(n->data);
        _walk(n->right);
    }
    _walk(t->root);
}

static void _destroy(BSTNode *n) {
    if (!n) return;
    _destroy(n->left);
    _destroy(n->right);
    free(n);
}
void bst_destroy(BST *t) {
    if (t) { _destroy(t->root); free(t); }
}
