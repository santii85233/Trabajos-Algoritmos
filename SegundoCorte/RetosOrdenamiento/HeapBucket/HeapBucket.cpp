#include <iostream>
#include <vector>
#include <cstdlib>
#include <chrono>
using namespace std;

// Retos de Heap y Bucket

int cambios = 0;
int comparaciones = 0;

// RETO 1: Heapsort de maximos: la raíz es el mayor 
void heapifyMax(int arr[], int n, int i) {
    int mayor = i;   // Se supone que el mayor es el padre
    int izq = 2 * i + 1;
    int der = 2 * i + 2;
    if (izq < n) {
        comparaciones++;
        if (arr[izq] > arr[mayor]) mayor = izq;
    }
    if (der < n) {
        comparaciones++;
        if (arr[der] > arr[mayor]) mayor = der;
    }
    if (mayor != i) {
        int temp = arr[i];
        arr[i] = arr[mayor];
        arr[mayor] = temp;
        cambios++;
        heapifyMax(arr, n, mayor);
    }
}

void heapSortMax(int arr[], int n) {
    cambios = 0;
    comparaciones = 0;
    for (int i = n / 2 - 1; i >= 0; i--) { // Se construye el heap
        heapifyMax(arr, n, i);
    }
    for (int i = n - 1; i > 0; i--) {
        int temp = arr[0]; // La raíz se manda al final
        arr[0] = arr[i];
        arr[i] = temp;
        cambios++;
        heapifyMax(arr, i, 0);
    }
    cout << "El array ordenado con heap sort de maximos es: [";
    for (int i = 0; i < n; i++) cout << arr[i] << (i < n - 1 ? ", " : "");
    cout << "], realizando " << cambios << " cambios y " << comparaciones << " comparaciones.\n";
}

// Heapsort de minimos: la raiz es el menor (se cambian los > por <)
void heapifyMin(int arr[], int n, int i) {
    int menor = i; // Se supone que el menor es el padre
    int izq = 2 * i + 1;
    int der = 2 * i + 2;
    if (izq < n) {
        comparaciones++;
        if (arr[izq] < arr[menor]) menor = izq;
    }
    if (der < n) {
        comparaciones++;
        if (arr[der] < arr[menor]) menor = der;
    }
    if (menor != i) {
        int temp = arr[i];
        arr[i] = arr[menor];
        arr[menor] = temp;
        cambios++;
        heapifyMin(arr, n, menor);
    }
}

void heapSortMin(int arr[], int n) {
    cambios = 0;
    comparaciones = 0;
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapifyMin(arr, n, i);
    }
    for (int i = n - 1; i > 0; i--) {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        cambios++;
        heapifyMin(arr, i, 0);
    }
    cout << "El array ordenado con heap sort de minimos es: [";
    for (int i = 0; i < n; i++) cout << arr[i] << (i < n - 1 ? ", " : "");
    cout << "], realizando " << cambios << " cambios y " << comparaciones << " comparaciones.\n";
}

// RETO 2: Bucket sort con k cubetas, cada cubeta se ordena con insertion sort
void bucketSort(int arr[], int n, int k) {
    cambios = 0;
    comparaciones = 0;
    int maximo = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > maximo) maximo = arr[i];
    }
    vector<vector<int>> cubetas(k); // Se crean las cubetas vacias
    for (int i = 0; i < n; i++) {
        int posicion = arr[i] * k / (maximo + 1); // Se selecciona la cubeta que le toca al número
        cubetas[posicion].push_back(arr[i]);
    }
    int pos = 0;
    for (int c = 0; c < k; c++) {
        for (int i = 1; i < (int)cubetas[c].size(); i++) { // Insertion sort dentro de la cubeta
            int key = cubetas[c][i];
            int j = i - 1;
            while (j >= 0) {
                comparaciones++;
                if (cubetas[c][j] > key) {
                    cubetas[c][j + 1] = cubetas[c][j];
                    j--;
                } else {
                    break;
                }
            }
            cubetas[c][j + 1] = key;
            cambios++;
        }
        for (int i = 0; i < (int)cubetas[c].size(); i++) {
            arr[pos] = cubetas[c][i];
            pos++;
        }
    }
}

int main() {
    // RETO 1
    
    int datosMax[] = {64, 25, 12, 22, 11, 90, 45, 33};
    int datosMin[] = {64, 25, 12, 22, 11, 90, 45, 33};
    heapSortMax(datosMax, 8);
    heapSortMin(datosMin, 8);

    // RETO 2
    
    // Se crea un arreglo de 1000 números aleatorios, el mismo para las dos pruebas
    int n = 1000;
    int datosBucket1[1000];
    int datosBucket2[1000];
    for (int i = 0; i < n; i++) {
        datosBucket1[i] = rand() % 10000;
        datosBucket2[i] = datosBucket1[i];
    }

    cout << "\nBucket sort con 1000 datos\n";

    auto inicio = chrono::steady_clock::now();
    bucketSort(datosBucket1, n, 5);
    auto final = chrono::steady_clock::now();
    chrono::duration<double> duracion = final - inicio;
    cout << "5 cubetas: " << cambios << " cambios, " << comparaciones << " comparaciones y " << duracion.count() << " segundos\n";

    inicio = chrono::steady_clock::now();
    bucketSort(datosBucket2, n, 50);
    final = chrono::steady_clock::now();
    duracion = final - inicio;
    cout << "50 cubetas: " << cambios << " cambios, " << comparaciones << " comparaciones y " << duracion.count() << " segundos\n";

    return 0;
}

/*
 RETO 1: Heapsort de minimos, ¿que cambio?

 1. En heapify se cambian los > por < y la variable mayor pasa a ser menor: el padre
    tiene que ser menor que sus hijos, asi la raiz del heap es el minimo.
 2. Como el algoritmo manda la raiz al final del arreglo en cada vuelta, ahora se van
    al final los menores y el arreglo queda ordenado de MAYOR a MENOR:
    [90, 64, 45, 33, 25, 22, 12, 11]. Para dejarlo de menor a mayor habria que
    invertirlo al final o usar otro arreglo.
 3. Lo demas es igual: construir el heap, intercambiar la raiz con el ultimo y volver a arreglar.
    Con los 8 datos: maximos 20 cambios y 27 comparaciones, minimos 20 cambios y 28 comparaciones.

 RETO 2: Bucket Sort con 5 y con 50 cubetas (1000 datos, los mismos en las dos pruebas)

 Cubetas | Comparaciones | Cambios
 5       | 51357         | 995
 50      | 5748          | 950

 Con 5 cubetas cada una queda con unos 200 datos y el insertion sort de cada cubeta hace
 muchas comparaciones. Con 50 quedan unos 20 por cubeta y las comparaciones bajan casi 9 veces.
 Mas cubetas no es gratis (hay que crearlas y recorrerlas aunque queden vacias), por eso
 hay un punto donde dejan de ayudar.
*/
