// Sesion 40 — Grafos: matriz de adyacencia frente a lista de adyacencia
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

const vector<string> NOMBRES = {"CENTRO","NORTE","SUR","ORIENTE","OCCIDENTE",
                                "CHAPINERO","USAQUEN","BOSA","VEREDA"};
const vector<pair<int,int>> ARISTAS = {{0, 1},  // Centro -> Norte
    {1, 4},  // Norte -> Occidente
    {0, 2},  // Centro -> Sur
    {0, 3},  // Centro -> Oriente
    {1, 5},  // Norte -> Chapinero
    {2, 7},  // Sur -> Bosa
    {3, 6},  // Oriente -> Usaquen
    {5, 6},  // Chapinero -> Usaquen
    {4, 7},  // Occidente -> Bosa
    {7, 8},  // Bosa -> Vereda
    {8, 1},  // Vereda -> Norte
    {7, 5},  // Bosa -> Chapinero
    {5, 8},  // Chapinero -> Vereda
    {2, 6},  // Sur -> Usaquen
    {6, 8},  // Usaquen -> Vereda
    {5, 2},  // Chapinero -> Sur

};
const int N = 9;

int main() {
    // ---------- Representacion 1: matriz de adyacencia ----------
    vector<vector<int>> matriz(N, vector<int>(N, 0));
    for (auto [u, v] : ARISTAS) { matriz[u][v] = 1; matriz[v][u] = 1; }  // no dirigido: simetrica

    cout << "MATRIZ DE ADYACENCIA\n            ";
    for (auto& n : NOMBRES) cout << setw(5) << n.substr(0, 3);
    cout << endl;
    for (int i = 0; i < N; i++) {
        cout << setw(11) << NOMBRES[i] << " ";
        for (int j = 0; j < N; j++) cout << setw(5) << matriz[i][j];
        cout << endl;
    }

    // ---------- Representacion 2: lista de adyacencia ----------
    vector<vector<int>> lista(N);
    for (auto [u, v] : ARISTAS) { lista[u].push_back(v); lista[v].push_back(u); }
    for (auto& v : lista) sort(v.begin(), v.end());

    cout << "\nLISTA DE ADYACENCIA" << endl;
    for (int i = 0; i < N; i++) {
        cout << "  " << setw(10) << NOMBRES[i] << " -> ";
        for (size_t k = 0; k < lista[i].size(); k++) {
            cout << NOMBRES[lista[i][k]];
            if (k + 1 < lista[i].size()) cout << ", ";
        }
        cout << endl;
    }

    cout << "\nGRADO DE CADA VERTICE (cuantas vias salen de el)" << endl;
    for (int i = 0; i < N; i++) {
        int gMat = 0;
        for (int j = 0; j < N; j++) gMat += matriz[i][j];   // recorrer la fila: O(N)
        int gLis = (int)lista[i].size();                    // leer el tamano: O(1)
        cout << "  " << setw(10) << NOMBRES[i] << ": " << gLis
             << (gMat == gLis ? "" : "  <-- DISCREPANCIA") << endl;
    }

    int E = (int)ARISTAS.size();
    cout << "\nV = " << N << " vertices,  E = " << E << " aristas" << endl;
    cout << "  Matriz : " << N * N << " casillas en memoria. Existe arista? O(1). Recorrer vecinos: O(V) = " << N << " casillas." << endl;
    cout << "  Lista  : " << 2 * E << " referencias en memoria. Existe arista? O(grado). Recorrer vecinos: O(grado)." << endl;
    double dens = 2.0 * E / (N * (N - 1.0));
    cout << "  Densidad = 2E / (V(V-1)) = " << fixed << setprecision(2) << dens
         << "  ->  grafo " << (dens > 0.5 ? "DENSO: conviene matriz" : "DISPERSO: conviene lista") << endl;

    auto hayViaMatriz = [&](int u, int v) { return matriz[u][v] == 1; };
    auto hayViaLista  = [&](int u, int v) { return find(lista[u].begin(), lista[u].end(), v) != lista[u].end(); };
    for (auto [u, v] : vector<pair<int,int>>{{1,0},{1,8},{5,6}})
        cout << "  Conecta " << NOMBRES[u] << " con " << NOMBRES[v] << "? matriz="
             << (hayViaMatriz(u,v) ? "true" : "false") << "  lista="
             << (hayViaLista(u,v) ? "true" : "false") << endl;
    return 0;
}
