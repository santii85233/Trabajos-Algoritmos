#include <iostream>
using namespace std;

/* Bubble Sort */
void bubbleSort(int arr[], int n) {
    int cambios = 0;
    int comparaciones = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            comparaciones++; // Cuenta cada comparación del if
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                cambios++;   // Cuenta el intercambio
            }
        }
    }
    
    cout << "El array ordenado con bubble sort es: [";
    for(int i = 0; i < n; i++) cout << arr[i] << (i < n - 1 ? ", " : "");
    cout << "], realizando " << cambios << " cambios y " << comparaciones << " comparaciones.\n";
}

/* Selection Sort */
void selectionSort(int arr[], int n) {
    int cambios = 0;
    int comparaciones = 0;
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            comparaciones++; 
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        cambios++;
        int temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
        }
        
        cout << "El array ordenado con selection sort es: [";
        for(int i = 0; i < n; i++) cout << arr[i] << (i < n - 1 ? ", " : "");
        cout << "], realizando " << cambios << " cambios y " << comparaciones << " comparaciones.\n";
    }

/* Insertion Sort */
void insertionSort(int arr[], int n) {
    int cambios = 0;
    int comparaciones = 0;
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            comparaciones++;
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
        cambios++;
    }

    
    cout << "El array ordenado con insertion sort es: [";
    for(int i = 0; i < n; i++) cout << arr[i] << (i < n - 1 ? ", " : "");
    cout << "], realizando " << cambios << " cambios y " << comparaciones << " comparaciones.\n";
}

int main() {
    int n = 8;
    
    // Se crean copias independientes para probar cada algoritmo con los datos originales desordenados
    int datosBubble[] = {64, 25, 12, 22, 11, 90, 45, 33};
    int datosSelection[] = {64, 25, 12, 22, 11, 90, 45, 33};
    int datosInsertion[] = {64, 25, 12, 22, 11, 90, 45, 33};

    // Ejecución de los métodos
    bubbleSort(datosBubble, n);
    selectionSort(datosSelection, n);
    insertionSort(datosInsertion, n);

    return 0;
}
