//QUIZ 28 DE OCTUBRE 2026

#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct Nodo {
    string dato;
    string nombre;
    Nodo* izq;
    Nodo* der;
    Nodo(string d, string n = "") : dato(d), nombre(n), izq(nullptr), der(nullptr) {}
};

void preorden(Nodo* n, vector<string>& s) {
    if (n == nullptr) return;
    s.push_back(n->dato);
    preorden(n->izq, s);
    preorden(n->der, s);
}

void inorden(Nodo* n, vector<string>& s) {
    if (n == nullptr) return;
    inorden(n->izq, s);
    s.push_back(n->dato);
    inorden(n->der, s);
}

void postorden(Nodo* n, vector<string>& s) {
    if (n == nullptr) return;
    postorden(n->izq, s);
    postorden(n->der, s);
    s.push_back(n->dato);
}

int altura(Nodo* n) {
    if (n == nullptr) return -1;
    return 1 + max(altura(n->izq), altura(n->der));
}

int contar(Nodo* n) {
    if (n == nullptr) return 0;
    return 1 + contar(n->izq) + contar(n->der);
}

int contarHojas(Nodo* n) {
    if (n == nullptr) return 0;
    if (n->izq == nullptr && n->der == nullptr) return 1;
    return contarHojas(n->izq) + contarHojas(n->der);
}

vector<string> porNiveles(Nodo* raiz) {
    vector<string> s;
    if (raiz == nullptr) return s;
    queue<Nodo*> q; q.push(raiz);
    while (!q.empty()) {
        Nodo* n = q.front(); q.pop();
        s.push_back(n->dato);
        if (n->izq) q.push(n->izq);
        if (n->der) q.push(n->der);
    }
    return s;
}

void liberar(Nodo* n) {
    if (n == nullptr) return;
    liberar(n->izq);
    liberar(n->der);
    delete n;
}

void mostrar(const string& titulo, const vector<string>& v) {
    if (!titulo.empty()) cout << titulo << ": ";
    for (size_t i = 0; i < v.size(); i++) {
        cout << v[i];
        if (i + 1 < v.size()) cout << " -> ";
    }
    cout << endl;
}

Nodo* insertar(Nodo*& raiz, string clave, string nombre="") {
    if (raiz == nullptr) {
        raiz = new Nodo(clave, nombre);
        return raiz;
    }
    if(clave < raiz->dato) {
        return insertar(raiz->izq, clave, nombre);
    } else if (clave > raiz->dato) {
        return insertar(raiz->der, clave, nombre);
    } else {
        return raiz; 
    }
}

Nodo* buscar(Nodo* raiz, string clave, vector<string>* pasos = nullptr) {
    if (raiz == nullptr) return nullptr;
    if (pasos != nullptr) {
        pasos->push_back(raiz->dato);
    }
    if (clave < raiz->dato) {
        return buscar(raiz->izq, clave, pasos);
    } if (clave >raiz->dato) {
        return buscar(raiz->der, clave, pasos);
    }
    else {
        return raiz;
    }
}

Nodo* minimo(Nodo* raiz) {
    if (raiz == nullptr) return nullptr;
    while (raiz->izq != nullptr) {
        raiz = raiz->izq;
    }
    return raiz;
}

Nodo* maximo(Nodo* raiz) {
    if (raiz == nullptr) return nullptr;
    while (raiz->der != nullptr) {
        raiz = raiz->der;
    }
    return raiz;
}

Nodo* eliminar(Nodo*& raiz, string clave) {
    if (raiz == nullptr) return nullptr;
    if (clave < raiz->dato) {
        raiz->izq = eliminar(raiz->izq, clave);
    } else if (clave > raiz->dato) {
        raiz->der = eliminar(raiz->der, clave);
    } else {
        if (raiz->izq == nullptr) {
            Nodo* temp = raiz->der;
            delete raiz;
            return temp;
        } else if (raiz->der == nullptr) {
            Nodo* temp = raiz->izq;
            delete raiz;
            return temp;
        } else {
            Nodo* sucesor = minimo(raiz->der);
            raiz->dato = sucesor->dato;
            raiz->nombre = sucesor->nombre;
            raiz->der = eliminar(raiz->der, sucesor->dato);
        }
    }
    return raiz;
}

int hijos(Nodo* raiz, string clave) {
    Nodo* n = buscar(raiz, clave);
    if (n == nullptr) return -1;
    int h = 0;
    if (n->izq != nullptr) h++;
    if (n->der != nullptr) h++;
    return h;
}

int main() {
    Nodo* raiz = nullptr;
    for (string c : {"50", "30", "70", "20", "40", "60", "80", "35"}) {
        insertar(raiz, c);
    }
    
    vector<string> s; 
    inorden(raiz, s);
    mostrar("Inorden (queda ordenado)", s);

    cout << "minimo = " << minimo(raiz)->dato 
         << "  maximo = " << maximo(raiz)->dato
         << "  altura = " << altura(raiz) << endl;

    for (string objetivo : {"40", "65"}) {
        vector<string> p; 
        Nodo* r = buscar(raiz, objetivo, &p);
        cout << "buscar(" << objetivo << "): camino ";
        mostrar("", p);
        cout << "  =>  " << (r ? "ENCONTRADO" : "NO ESTA")
             << "  (" << p.size() << " comparaciones)" << endl;
    }

    const char* NOMBRE[] = {"caso 1: hoja, 0 hijos", "caso 2: un hijo", "caso 3: dos hijos"};
    for (string clave : {"20", "30", "50"}) {
        int k = hijos(raiz, clave);                 
        raiz = eliminar(raiz, clave);
        s.clear(); 
        inorden(raiz, s);
        cout << "eliminar(" << clave << ") [" << NOMBRE[k] << "] -> ";
        mostrar("", s);
    }

    Nodo* deg = nullptr;
    for (string c : {"10", "20", "30", "40", "50", "60", "70", "80"}) {
        insertar(deg, c);
    }
    cout << "\nBST con datos ordenados: altura = " << altura(deg) << " con 8 nodos (una lista enlazada)" << endl;
    cout << "BST con datos mezclados: altura = 3 con 8 nodos (log2(8) = 3)" << endl;

    liberar(raiz); 
    liberar(deg);
    return 0;
}
