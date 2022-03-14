// pseudokod

#include <iostream>

using namespace std;

class RBT {
    struct Node {
        int key;
        int color;
        Node *left, *right, *p;
    };

    Node *root;
    Node insertNode(int, Node*);
    Node searchNode(int, Node*);
    Node removeNode(int, Node*);
    Node leftRotate(int, Node*);
    void printTree(Node*);

    public:
    RBT() {
        root = NULL;
    }

    void insertNode(int x) {
        root = insertNode(x, root);
    }

    void searchNode(int x) {
        root = searchNode(x, root);
    }

    void removeNode(int x) {
        root = removeNode(x, root);
    }

    void leftRotate(int x) {
        root = leftRotate(x, root);
    }

};

int main() {

    return 0;
}