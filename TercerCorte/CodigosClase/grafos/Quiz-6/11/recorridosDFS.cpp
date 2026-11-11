#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int N = 9;
const vector<string> NOMBRES = {
    "CENTRO", "NORTE", "SUR", "ORIENTE", "OCCIDENTE",
    "CHAPINERO", "USAQUEN", "BOSA", "VEREDA"
};

vector<vector<int>> lista(N);

// ---------- DFS recursivo----------
void dfsRec(int u, vector<bool>& vis, vector<int>& orden) {
    vis[u] = true;              // el hilo de Ariadna
    orden.push_back(u);
    for (int v : lista[u])
        if (!vis[v]) dfsRec(v, vis, orden);
}

// ---------- DFS iterativo----------
vector<int> dfsIter(int inicio) {
    vector<bool> vis(N, false);
    vector<int> pila{inicio}, orden;
    while (!pila.empty()) {
        int u = pila.back(); pila.pop_back();   // LIFO
        if (vis[u]) continue;                   // pudo entrar dos veces
        vis[u] = true;
        orden.push_back(u);
        for (auto it = lista[u].rbegin(); it != lista[u].rend(); ++it)
            if (!vis[*it]) pila.push_back(*it);
    }
    return orden;
}

// imprimir ordenes de visita con nombres
void imprimir_orden(const string& titulo, const vector<int>& orden) {
    cout << titulo << "\n  orden de visita: ";
    for (size_t i = 0; i < orden.size(); ++i) {
        cout << NOMBRES[orden[i]] << (i + 1 < orden.size() ? " -> " : "");
    }
    cout << "\n\n";
}
void imprimir_componentes(const vector<vector<int>>& lista_actual) {
    vector<bool> vis(N, false);
    cout << "[";
    bool primera_comp = true;
    for (int s = 0; s < N; ++s) {
        if (!vis[s]) {
            vector<int> o;
            dfsRec(s, vis, o);
            if (!primera_comp) cout << ", ";
            cout << "[";
            for (size_t i = 0; i < o.size(); ++i) {
                cout << "'" << NOMBRES[o[i]] << "'" << (i + 1 < o.size() ? ", " : "");
            }
            cout << "]";
            primera_comp = false;
        }
    }
    cout << "]\n";
}

// detección de ciclo
bool explorar_ciclo(int u, int padre, const vector<bool>& vis_global, vector<bool>& visitado_local, const vector<vector<int>>& lista_act) {
    visitado_local[u] = true;
    for (int v : lista_act[u]) {
        if (!visitado_local[v]) {
            if (explorar_ciclo(v, u, vis_global, visitado_local, lista_act)) return true;
        } else if (v != padre) {
            return true; 
        }
    }
    return false;
}

bool hay_ciclo(const vector<vector<int>>& lista_act) {
    vector<bool> visitado(N, false);
    for (int s = 0; s < N; ++s) {
        if (!visitado[s]) {
            if (explorar_ciclo(s, -1, visitado, visitado, lista_act)) return true;
        }
    }
    return false;
}
int main() {
    // Definición de aristas originales
    vector<pair<int, int>> aristas = {
        {0, 1}, {1, 4}, {0, 2}, {0, 3}, {1, 5},
        {2, 7}, {3, 6}, {5, 6}, {4, 7}, {7, 8},
        {8, 1}, {7, 5}, {5, 8}, {2, 6}, {6, 8}, {5, 2}
    };

    // Construcción de la lista de adyacencia
    for (const auto& a : aristas) {
        lista[a.first].push_back(a.second);
        lista[a.second].push_back(a.first);
    }
    for (auto& v : lista) {
        sort(v.begin(), v.end());
    }

    //Prueba DFS Recursivo
    vector<bool> vis(N, false);
    vector<int> orden_rec;
    dfsRec(0, vis, orden_rec);
    imprimir_orden("DFS RECURSIVO desde CENTRO", orden_rec);

    //Prueba DFS Iterativo
    vector<int> orden_iter = dfsIter(0);
    imprimir_orden("DFS ITERATIVO (con pila explicita) desde CENTRO", orden_iter);

    for (const auto& a : aristas) {
        lista[a.first].push_back(a.second);
        lista[a.second].push_back(a.first);
    }
    for (auto& v : lista) {
        sort(v.begin(), v.end());
    }

    //componentes conexas (red completa)
    cout << "COMPONENTES CONEXAS de la red completa: ";
    imprimir_componentes(lista);

    // Red con un punto aislado y un par suelto
    vector<vector<int>> lista_rota(N);
    vector<pair<int, int>> aristas_rotas = {{0, 1}, {0, 2}, {3, 6}};
    for (const auto& par : aristas_rotas) {
        lista_rota[par.first].push_back(par.second);
        lista_rota[par.second].push_back(par.first);
    }
    for (auto& v : lista_rota) {
        sort(v.begin(), v.end());
    }

    // Guardamos la original y cambiamos temporalmente a la rota
    vector<vector<int>> lista_orig = lista;
    lista = lista_rota;

    cout << "COMPONENTES de una red con tramos cortados: ";
    imprimir_componentes(lista_rota);

    // Restauramos la original para la verificación de ciclos
    lista = lista_orig;

    //detección de ciclo
    cout << "¿La red tiene algun circuito? " << (hay_ciclo(lista) ? "True" : "False") << "\n";

    return 0;
}