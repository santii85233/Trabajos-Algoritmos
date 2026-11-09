// ============================================================
//  Laboratorio integrador · Corte 3 · RETO 2  (25 puntos)
//  Sesiones 37 y 38 — Rotaciones y arboles AVL
//  Sistema: RedAcopio — el indice se degrada con codigos consecutivos
//
//  Este archivo NO tiene main(): el main esta en pruebas_r2.cpp
//  MODIFIQUE SOLO ESTE ARCHIVO.  NO TOQUE pruebas_r2.cpp
//  Compile y ejecute:
//     g++ -std=c++17 -g -o pruebas_r2 balanceo.cpp pruebas_r2.cpp
//     ./pruebas_r2
// ============================================================

#include <algorithm>
#include "avl.h"
using namespace std;

int  alt(Nodo* n)    { return n == nullptr ? -1 : n->alt; }
int  fe(Nodo* n)     { return n == nullptr ? 0 : alt(n->izq) - alt(n->der); }
void recalc(Nodo* n) { n->alt = 1 + max(alt(n->izq), alt(n->der)); }

Nodo* rotarDerecha(Nodo* y) {
    //        y                x
    //       / \              / \
    //      x   C    ==>     A   y
    //     / \                  / \
    //    A   B                B   C
    Nodo* x = y->izq;
    Nodo* B = x->der;
    x->der = y;
    y->izq = B;
    recalc(y); recalc(x);      // primero el que BAJA, luego el que SUBE
    return x;
}
#include <algorithm>
#include <cstdlib>      // para abs()
#include "avl.h"
using namespace std;

// alt, fe, recalc y rotarDerecha se quedan igual

Nodo* rotarIzquierda(Nodo* x) {
    Nodo* y = x->der;
    Nodo* B = y->izq;
    y->izq = x;
    x->der = B;
    recalc(x); recalc(y);      // primero el que BAJA (x), luego el que SUBE (y)
    return y;
}

Nodo* insertar(Nodo* n, int clave) {
    // FASE 1
    if (n == nullptr) return new Nodo(clave);
    if      (clave < n->clave) n->izq = insertar(n->izq, clave);
    else if (clave > n->clave) n->der = insertar(n->der, clave);
    else return n;

    // FASE 2
    recalc(n);

    // FASE 3
    int b = fe(n);

    if (b > 1 && clave < n->izq->clave) {            // LL
        return rotarDerecha(n);
    }
    if (b < -1 && clave > n->der->clave) {           // RR
        return rotarIzquierda(n);
    }
    if (b > 1 && clave > n->izq->clave) {            // LR
        n->izq = rotarIzquierda(n->izq);
        return rotarDerecha(n);
    }
    if (b < -1 && clave < n->der->clave) {           // RL
        n->der = rotarDerecha(n->der);
        return rotarIzquierda(n);
    }
    return n;
}