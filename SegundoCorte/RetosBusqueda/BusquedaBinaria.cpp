#include <vector>
#include <iostream>
using namespace std;

// Retorna un índice i con a[i]==x, o -1.

// Precondición: a ordenado de forma no decreciente.
int busquedaBinaria(const vector<int>& a, int x) {
    int izq = 0, der = (int)a.size() - 1;   // rango CERRADO  izq, der]

    while  (izq <= der) {
        int mid = izq + (der - izq) / 2;     // evita desbordamiento
        if (a[mid] == x) return mid;
        else if (a[mid] <  x) izq = mid + 1;   // descarta mitad izquierda
        else der = mid - 1;   // descarta mitad derecha
    }
    return -1;                            // rango vacío ⇒ no está
}

//recursiva(Reto1)

int binariaRec(const vector<int>& a, int x, int izq, int der) {
    int mid = (izq + der) / 2;

    // caso base: vacío y retorno de posición (Reto1)
    if (izq > der) return mid+1;        

    // descarta mitad derecha y si se repite el elemento, devuelve la primera posición (Reto3)
    if (x <= a[mid]) return binariaRec(a, x, izq, mid - 1); 
    
    // descarta mitad izquierda
    else return binariaRec(a, x, mid + 1, der); 
}

int main(){
    vector<int> v = {
        1,2,3,4,5,6,7,8,9,9,9,9,12,13,14,15,16,17,18,19,20,
        21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
        41,42,43,44,45,47,48,49,50
    };
    vector<int> v2 = {
       1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20
    };
    cout<<"Índice del primer elemento repetido 9 es el: " << binariaRec(v, 9, 0, (int)v.size() - 1) << endl;
    cout<<"Índice donde debe ir el elemento 16 es: " << binariaRec(v2, 16, 0, (int)v2.size() - 1) << endl;

    return 0;
}