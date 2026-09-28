#include <iostream>
#include <cstdlib>
#include <chrono>
using namespace std;

// Retos de Merge y Quick

int cambios = 0;
int comparaciones = 0;

// RETO 1: Quicksort en el sitio con dos índices que se cruzan 
int particion(int arr[], int inicio, int fin) {
    int pivote = arr[inicio]; // El pivote es el primer elemento
    int i = inicio - 1;       // i empieza a la izquierda
    int j = fin + 1;          // j empieza a la derecha
    while (true) {
        i++;
        comparaciones++;
        while (arr[i] < pivote) { // i avanza mientras el elemento sea menor al pivote
            i++;
            comparaciones++;
        }
        j--;
        comparaciones++;
        while (arr[j] > pivote) { // j retrocede mientras el elemento sea mayor al pivote
            j--;
            comparaciones++;
        }
        if (i >= j) return j; // Si los indices se cruzan, se termina
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        cambios++;
    }
}

void quickRec(int arr[], int inicio, int fin) {
    if (inicio < fin) {
        int p = particion(arr, inicio, fin);
        quickRec(arr, inicio, p);   // Lado izquierdo
        quickRec(arr, p + 1, fin);  // Lado derecho
    }
}

void quickSort(int arr[], int n) {
    cambios = 0;
    comparaciones = 0;
    quickRec(arr, 0, n - 1);
}

int main() {
    // RETO 1

    int datosQuick[] = {64, 25, 12, 22, 11, 90, 45, 33};
    quickSort(datosQuick, 8);
    cout << "El array ordenado con quick sort es: [";
    for (int i = 0; i < 8; i++) cout << datosQuick[i] << (i < 7 ? ", " : "");
    cout << "], realizando " << cambios << " cambios y " << comparaciones << " comparaciones.\n";

    // RETO 2
    
    // Se crea un arreglo de 500 números aleatorios
    int n = 500;
    int listaAleatoria[500];
    for (int i = 0; i < n; i++) {
        listaAleatoria[i] = rand() % 10000;
    }

    // Se copia el mismo arreglo y se ordena con el mismo quickSort para tener la lista ya ordenada
    // (el peor caso para el primer elemento como pivote). Esta ordenada no se mide.
    int listaOrdenada[500];
    for (int i = 0; i < n; i++) listaOrdenada[i] = listaAleatoria[i];
    quickSort(listaOrdenada, n);

    cout << "\nQuick sort con 500 datos\n";

    auto inicio = chrono::steady_clock::now();
    quickSort(listaAleatoria, n);
    auto final = chrono::steady_clock::now();
    chrono::duration<double> duracion = final - inicio;
    cout << "Lista aleatoria: " << cambios << " cambios, " << comparaciones << " comparaciones y " << duracion.count() << " segundos\n";

    inicio = chrono::steady_clock::now();
    quickSort(listaOrdenada, n);
    final = chrono::steady_clock::now();
    duracion = final - inicio;
    cout << "Lista ordenada: " << cambios << " cambios, " << comparaciones << " comparaciones y " << duracion.count() << " segundos\n";

    return 0;
}

/*
 RETO 1: Quicksort en el sitio

 Se ordena sobre el mismo arreglo, sin crear arreglos nuevos. Hay dos indices: i avanza desde
 la izquierda mientras arr[i] < pivote y j retrocede desde la derecha mientras arr[j] > pivote.
 Cuando los dos se detienen se intercambian y se sigue hasta que se cruzan (i >= j).
 El pivote es el primer elemento y el arreglo se parte en (inicio, j) y (j+1, fin).
 Con los 8 datos de clase: 6 cambios y 39 comparaciones.

 RETO 2: caso que hace pesimo al Quicksort

 Con el primer elemento como pivote, un arreglo ya ordenado siempre deja el pivote en un
 extremo: una parte queda vacia y la otra con n-1 elementos, entonces se parte n veces
 en vez de log n veces. Con 500 datos (los mismos datos primero aleatorios y luego ordenados):

 Arreglo    | Comparaciones | Cambios
 Aleatorio  | 6836          | 1085
 Ordenado   | 125758        | 10

 Con el ordenado hace unas 18 veces mas comparaciones (casi n^2/2 = 125000)
 y tarda unas 6 veces mas.
*/
