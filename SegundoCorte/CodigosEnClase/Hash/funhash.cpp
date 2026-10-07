#include <iostream>
#include <vector>
#include <string>
#include <list>

using namespace std;

class TablaHash{
    protected:
        int cap;
        int n;
        vector<list<pair<string,string>>> cubetas;
    public:
        TablaHash(int capacidad=8):cap(capacidad),n(0),cubetas(capacidad){}

    int hashear(const string & clave) const {
        unsigned long long h = 0;
        for (unsigned char c : clave) h = (h * 31 + c) % cap;
        return (int)h;
    }
    void insertar(const string& clave, const string& valor) {
        int i = hashear(clave);
        for (auto& par : cubetas[i]) {
            if (par.first == clave) { par.second = valor; return; }   // ACTUALIZA
        }
        cubetas[i].push_back({clave, valor});
        n++;
        if (factorCarga() > 0.75) {
            redimensionar();
        }
    }
    bool buscar(const string& clave, string& salida) const {
        int i = hashear(clave);
        for (const auto& par : cubetas[i]) {
            if (par.first == clave) { salida = par.second; return true; }
        }
        return false;
    }
    bool eliminar(const string& clave) {
        int i = hashear(clave);
        for (auto it = cubetas[i].begin(); it != cubetas[i].end(); ++it) {
            if (it->first == clave) { cubetas[i].erase(it); n--; return true; }
        }
        return false;
    }
    void redimensionar() {
        // Guardamos una copia de las cubetas actuales
        vector<list<pair<string, string>>> viejas = cubetas; 

        // TODO 1: duplicar cap
        cap = cap * 2; 

        // TODO 2: cubetas.assign(cap, list<pair<string, string>>());
        cubetas.assign(cap, list<pair<string, string>>());

        // Reiniciamos el contador de elementos totales
        n = 0; 
        // TODO 3: recorrer 'viejas' e insertar cada par otra vez
        for (const auto& lista : viejas) {
            for (const auto& par : lista) {
                insertar(par.first, par.second); 
            }
        }
    }
    int factorCarga() const { return (float)n / cap; }

    int hashMala(const string& clave) const {
        char c = clave[0];
        for (int i = 1; i < 4 && i < clave.size(); ++i) {
            c += clave[i];
        }
        return (int)c % cap;
    }

    int capacidad() const { return cap; }

};

// 3. Comparar dos funciones hash. Agreguen una segunda función, 
//la "mala", que solo suma los 4 primeros caracteres de la clave: 
//Carguen los 12 estudiantes con cada función e impriman: 
//capacidad final, distribución, factor de carga, 
//cubeta más llena y cubetas vacías.


int main() {
    TablaHash tabla;
    tabla.insertar("EST-2026-0101", "Ana Torres");
    tabla.insertar("EST-2026-0107", "Pedro Ruiz");
    tabla.insertar("EST-2026-0102", "Carlos Rojas");
    tabla.insertar("EST-2026-0108", "Camila Diaz");
    tabla.insertar("EST-2026-0103", "Diego Pardo");
    tabla.insertar("EST-2026-0109", "Luis Herrera");
    tabla.insertar("EST-2026-0104", "Sofia Mejia");
    tabla.insertar("EST-2026-0110", "Valentina Cruz");
    tabla.insertar("EST-2026-0105", "Juan Gomez");
    tabla.insertar("EST-2026-0111", "Andres Vega");
    tabla.insertar("EST-2026-0106", "Maria Lopez");
    tabla.insertar("EST-2026-0112", "Laura Castro");
    string valor;

    if (tabla.buscar("EST-2026-0107", valor)) {
        cout << "Encontrado: " << valor << endl;
    } else {
        cout << "No encontrado" << endl;
    }
    tabla.redimensionar();
    for (int i = 0; i < tabla.capacidad(); ++i) {
        cout << "Cubeta " << i << ": ";
        for (const auto& par : tabla.cubetas[i]) {
            cout << "(" << par.first << ", " << par.second << ") ";
        }
        cout << endl;
    }
    cout << "Hash mala: " << tabla.hashMala("EST-2026-0107") << endl;

}