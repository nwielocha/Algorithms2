// Czarnych musi być wszedzie tyle samo
// wartownicy też wliczaja sie jako czarne
// 1. każdy węzeł mam przypisany kolor: czerwony lub czarny
// 2. korzeń jest czarny
// 3. liście są czarne; przyjmujemy wariant drzewa z
// wartownikami - liśćmi są wartownicy
// 4. czerwony węzeł nie może mieć czerwonego syna
// 5. na każdej ścieżce od korzenia do liści jest tyle samo
// czarnych węzłów

#include <iostream>

using namespace std;

struct Node {
    bool color;
    int key;
    Node *left, *right, *p;
};

struct Node *root;

void leftRotate(Node *node) {
    Node *x = node->right;
    Node *y = x->left;

    if (y->left != nullptr)
        y->left->p = x;

    y->p = x->p;

    if (x->p == nullptr)
        root = y;
    else if (x == x->p->left)
        x->p->left = y;
    else
        x->p->right = y;

    y->left = x;
    x->p = y;
}

void rightRotate(Node *node) {
    Node *x = node->left;
    Node *y = x->right;

    
}

int main() {

    return 0;
}
