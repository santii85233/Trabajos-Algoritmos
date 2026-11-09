// ============================================================
//  Laboratorio integrador · Corte 3 · RETO 4  (25 puntos)
//  Sesiones 41 y 43 — DFS, componentes conexas y vias criticas
//  Sistema: RedAcopio — que vias no pueden cerrarse
//
//  Este archivo NO tiene main(): el main esta en pruebas_r4.cpp
//  MODIFIQUE SOLO ESTE ARCHIVO.  NO TOQUE pruebas_r4.cpp ni red.h
//  Compile y ejecute:
//     g++ -std=c++17 -g -o pruebas_r4 conectividad.cpp pruebas_r4.cpp
//     ./pruebas_r4
// ============================================================
// @SantiagoArteaga
#include <vector>
#include <string>
#include "red.h"
using namespace std;

int cuantasComponentes(const vector<vector<int>>& g) {
    vector<bool> visitado(g.size(), false);
    int componentes = 0;

    for (size_t s = 0; s < g.size(); s++) {
        if (visitado[s]) continue;      // ya pertenece a una componente
        componentes++;                  // DFS nuevo = componente nueva

        vector<int> pila{(int)s};
        while (!pila.empty()) {
            int u = pila.back(); pila.pop_back();
            if (visitado[u]) continue;
            visitado[u] = true;
            for (int v : g[u])
                if (!visitado[v]) pila.push_back(v);
        }
    }
    return componentes;
}

vector<string> viasCriticas() {
    vector<string> criticas;
    for (size_t i = 0; i < ARISTAS.size(); i++) {
        // red SIN la arista i
        vector<pair<int,int>> sin;
        for (size_t j = 0; j < ARISTAS.size(); j++)
            if (j != i) sin.push_back(ARISTAS[j]);

        if (cuantasComponentes(construir(sin)) > 1)
            criticas.push_back(NOMBRES[ARISTAS[i].first] + "-" + NOMBRES[ARISTAS[i].second]);
    }
    return criticas;
}