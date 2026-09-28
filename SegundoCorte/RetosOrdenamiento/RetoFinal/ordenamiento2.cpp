#include <iostream>
#include <string>
#include <vector>
#include <chrono>
using namespace std;

// Reto final: tabla de comparacion de todos los metodos de ordenamiento
// Se prueba el ejercicio ordenamiento2 imprimiendo la lista ordenada, las comparaciones, los intercambios y el tiempo

int cambios = 0;
int comparaciones = 0;

/* Bubble Sort con bandera */
void bubbleSort(vector<int>& arr) {
    cambios = 0;
    comparaciones = 0;
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            comparaciones++;
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
                cambios++;
            }
        }
        if (!swapped) break;
    }
}

/* Selection Sort */
void selectionSort(vector<int>& arr) {
    cambios = 0;
    comparaciones = 0;
    int n = arr.size();
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
}

/* Insertion Sort */
void insertionSort(vector<int>& arr) {
    cambios = 0;
    comparaciones = 0;
    for (int i = 1; i < (int)arr.size(); i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0) {
            comparaciones++;
            if (arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            } else {
                break;
            }
        }
        arr[j + 1] = key;
        cambios++;
    }
}

// Merge Sort y Quicksort

/* Mergesort: divide la lista en sublistas mas pequeñas, las ordena y luego las combina.
   cambios: cada elemento que se escribe en arr al mezclar */
void mergeSort(vector<int>& arr) {
    int n = arr.size();
    if (n > 1) {
        int mid = n / 2;
        vector<int> leftHalf(arr.begin(), arr.begin() + mid);
        vector<int> rightHalf(arr.begin() + mid, arr.end());

        mergeSort(leftHalf);
        mergeSort(rightHalf);

        int i = 0, j = 0, k = 0;
        int tamIzq = leftHalf.size();
        int tamDer = rightHalf.size();

        while (i < tamIzq && j < tamDer) {
            comparaciones++;
            if (leftHalf[i] < rightHalf[j]) {
                arr[k] = leftHalf[i];
                i++;
            } else {
                arr[k] = rightHalf[j];
                j++;
            }
            k++;
            cambios++;
        }

        while (i < tamIzq) {
            arr[k] = leftHalf[i];
            i++;
            k++;
            cambios++;
        }

        while (j < tamDer) {
            arr[k] = rightHalf[j];
            j++;
            k++;
            cambios++;
        }
    }
}

/* Quicksort: elige un pivote, los menores quedan a la izquierda y los mayores a la derecha.
   comparaciones: cada elemento se compara 3 veces contra el pivote (menor, igual y mayor)
   cambios: cada elemento que se coloca en una lista nueva */
vector<int> quickSort(vector<int> arr) {
    int n = arr.size();
    if (n <= 1) {
        return arr;
    }
    int pivot = arr[n / 2];
    vector<int> left, middle, right;
    for (int a = 0; a < n; a++) if (arr[a] < pivot) left.push_back(arr[a]);
    for (int a = 0; a < n; a++) if (arr[a] == pivot) middle.push_back(arr[a]);
    for (int a = 0; a < n; a++) if (arr[a] > pivot) right.push_back(arr[a]);
    comparaciones += 3 * n;
    cambios += n;

    vector<int> resultado = quickSort(left);
    for (int a = 0; a < (int)middle.size(); a++) resultado.push_back(middle[a]);
    vector<int> derecha = quickSort(right);
    for (int a = 0; a < (int)derecha.size(); a++) resultado.push_back(derecha[a]);
    return resultado;
}

// Heapsort y Bucket Sort

/* Heapsort */
void heapify(vector<int>& arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n) {
        comparaciones++;
        if (arr[left] > arr[largest]) largest = left;
    }

    if (right < n) {
        comparaciones++;
        if (arr[right] > arr[largest]) largest = right;
    }

    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        cambios++;
        heapify(arr, n, largest);
    }
}

// Con heapify solo no se ordena: se construye el heap y la raiz se manda al final
void heapSort(vector<int>& arr) {
    cambios = 0;
    comparaciones = 0;
    int n = arr.size();
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
    for (int i = n - 1; i > 0; i--) {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        cambios++;
        heapify(arr, i, 0);
    }
}

/* Bucket Sort: cada cubeta se ordena con insertion sort (en vez de sort) para poder contar */
vector<int> bucketSort(vector<int> arr) {
    cambios = 0;
    comparaciones = 0;
    int n = arr.size();
    if (n == 0) {
        return arr;
    }

    int minValue = arr[0];
    int maxValue = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < minValue) minValue = arr[i];
        if (arr[i] > maxValue) maxValue = arr[i];
    }
    double bucketRange = (double)(maxValue - minValue) / n;

    vector<vector<int>> buckets(n);

    for (int a = 0; a < n; a++) {
        int index = (int)((arr[a] - minValue) / bucketRange);
        if (index == n) index--;
        buckets[index].push_back(arr[a]);
    }

    vector<int> sortedArr;
    for (int b = 0; b < n; b++) {
        for (int i = 1; i < (int)buckets[b].size(); i++) {
            int key = buckets[b][i];
            int j = i - 1;
            while (j >= 0) {
                comparaciones++;
                if (buckets[b][j] > key) {
                    buckets[b][j + 1] = buckets[b][j];
                    j--;
                } else {
                    break;
                }
            }
            buckets[b][j + 1] = key;
            cambios++;
        }
        for (int i = 0; i < (int)buckets[b].size(); i++) sortedArr.push_back(buckets[b][i]);
    }
    return sortedArr;
}

string nombres[7];
int tablaComp[7];
int tablaCambios[7];
double tablaTiempo[7];

// Imprime el arreglo ordenado y guarda la fila de la tabla
void guardar(int fila, string nombre, vector<int>& arr, double tiempo) {
    cout << "El array ordenado con " << nombre << " es: [";
    for (int i = 0; i < (int)arr.size(); i++) cout << arr[i] << (i < (int)arr.size() - 1 ? ", " : "");
    cout << "], realizando " << cambios << " cambios y " << comparaciones << " comparaciones.\n";
    cout << "La funcion tardo: " << tiempo << " segundos en completarse\n";

    nombres[fila] = nombre;
    tablaComp[fila] = comparaciones;
    tablaCambios[fila] = cambios;
    tablaTiempo[fila] = tiempo;
}

int main() {
    cout << fixed;        // Los tiempos se imprimen con decimales y no en notacion cientifica
    cout.precision(8);    // 8 decimales
    // Se selecciona la lista de clase
    vector<int> datos = {64, 25, 12, 22, 11, 90, 45, 33};
    vector<int> copia;
    chrono::duration<double> duracion;

    // Cada método trabaja con su propia copia de los datos y se mide el tiempo
    copia = datos;
    auto inicio = chrono::steady_clock::now();
    bubbleSort(copia);
    auto final = chrono::steady_clock::now();
    duracion = final - inicio;
    guardar(0, "bubble sort", copia, duracion.count());

    copia = datos;
    inicio = chrono::steady_clock::now();
    selectionSort(copia);
    final = chrono::steady_clock::now();
    duracion = final - inicio;
    guardar(1, "selection sort", copia, duracion.count());

    copia = datos;
    inicio = chrono::steady_clock::now();
    insertionSort(copia);
    final = chrono::steady_clock::now();
    duracion = final - inicio;
    guardar(2, "insertion sort", copia, duracion.count());

    copia = datos;
    cambios = 0;
    comparaciones = 0;
    inicio = chrono::steady_clock::now();
    mergeSort(copia);
    final = chrono::steady_clock::now();
    duracion = final - inicio;
    guardar(3, "merge sort", copia, duracion.count());

    copia = datos;
    cambios = 0;
    comparaciones = 0;
    inicio = chrono::steady_clock::now();
    copia = quickSort(copia);
    final = chrono::steady_clock::now();
    duracion = final - inicio;
    guardar(4, "quick sort", copia, duracion.count());

    copia = datos;
    inicio = chrono::steady_clock::now();
    heapSort(copia);
    final = chrono::steady_clock::now();
    duracion = final - inicio;
    guardar(5, "heap sort", copia, duracion.count());

    copia = datos;
    inicio = chrono::steady_clock::now();
    copia = bucketSort(copia);
    final = chrono::steady_clock::now();
    duracion = final - inicio;
    guardar(6, "bucket sort", copia, duracion.count());

    cout << "\nTabla de comparacion de los metodos de ordenamiento\n";
    cout << "Metodo          | Comparaciones | Intercambios | Tiempo (s)\n";
    for (int i = 0; i < 7; i++) {
        cout << nombres[i] << " | " << tablaComp[i] << " | " << tablaCambios[i] << " | " << tablaTiempo[i] << "\n";
    }
    return 0;
}

/*
 TABLA DE COMPARACION DE TODOS LOS METODOS (8 datos de clase)

 Metodo          | Comparaciones | Intercambios | Tiempo (s)
 BubbleSort      | 25            | 14           | 0.00000078
 SelectionSort   | 28            | 7            | 0.00000064
 InsertionSort   | 18            | 7            | 0.00000048
 MergeSort       | 16            | 24           | 0.00000562
 QuickSort       | 78            | 26           | 0.00001201
 HeapSort        | 27            | 20           | 0.00000116
 BucketSort      | 2             | 2            | 0.00000477

 Todos imprimen la misma lista ordenada:
 [11, 12, 22, 25, 33, 45, 64, 90]

 Que se cuenta en cada uno (se dejo la logica de ordenamiento2, solo se agregaron los contadores):
 Bubble, Heap: cada swap. Selection: un swap por vuelta. Insertion: una insercion de la llave por vuelta.
 Merge: cada elemento que se escribe en la lista al mezclar.
 Quick: como crea listas nuevas y no hace swaps, cada elemento se compara 3 veces contra el pivote
 (menor, igual, mayor) y en cambios se cuenta cada elemento que se coloca en una lista nueva.
 Bucket: las inserciones dentro de las cubetas. Se cambio sorted(bucket) por insertion sort en cada
 cubeta porque sorted no permite contar. Usa n cubetas (8).
 Heap: ordenamiento2 solo tenia heapify, se agrego heap_sort (construir el heap y mandar la raiz al final).

 Selection en C++ da 7 cambios y en Python 8 porque el ciclo for llega hasta n-1 en C++ y hasta n en Python.
 Los tiempos cambian en cada ejecucion y con solo 8 datos son muy pequeños, por eso
 se compara mejor con las comparaciones y los intercambios.
*/
