#include <iostream>
#include <string>
using namespace std;

// Retos de Ordenamientos Básicos: bubble, selection e insertion

int cambios = 0;
int comparaciones = 0;

/* Bubble Sort SIN bandera (version vieja, solo para comparar con la nueva) */
void bubbleSinBandera(int arr[], int n) {
    cambios = 0;
    comparaciones = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            comparaciones++; // Cuenta cada comparación de vecinos
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                cambios++;
            }
        }
    }
}

/* Bubble Sort CON bandera (Reto1) */
void bubbleSort(int arr[], int n) {
    cambios = 0;
    comparaciones = 0;
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false; // La bandera empieza en false en cada pasada
        for (int j = 0; j < n - i - 1; j++) {
            comparaciones++;
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true; // Hubo un intercambio
                cambios++;
            }
        }
        if (!swapped) break; // Si no hubo ningún intercambio la lista ya está ordenada
    }
}

/* Selection Sort */
void selectionSort(int arr[], int n) {
    cambios = 0;
    comparaciones = 0;
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i; // Se supone que el menor es el de la posición i
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
void insertionSort(int arr[], int n) {
    cambios = 0;
    comparaciones = 0;
    for (int i = 1; i < n; i++) {
        int key = arr[i]; // Se selecciona el elemento que se va a insertar
        int j = i - 1;
        while (j >= 0) {
            comparaciones++; // Aquí también se cuenta la comparación que falla
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

// Registro del proyecto: veces prestado y codigo del equipo
struct Equipo {
    int veces;
    string codigo;
};

/* Versiones para los registros (Reto 2 y 3): igual que las de arriba pero se compara por veces */
void bubbleSort(Equipo arr[], int n) {
    cambios = 0;
    comparaciones = 0;
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            comparaciones++;
            if (arr[j].veces > arr[j + 1].veces) {
                Equipo temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
                cambios++;
            }
        }
        if (!swapped) break;
    }
}

void selectionSort(Equipo arr[], int n) {
    cambios = 0;
    comparaciones = 0;
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            comparaciones++;
            if (arr[j].veces < arr[minIdx].veces) {
                minIdx = j;
            }
        }
        cambios++;
        Equipo temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
    }
}

void insertionSort(Equipo arr[], int n) {
    cambios = 0;
    comparaciones = 0;
    for (int i = 1; i < n; i++) {
        Equipo key = arr[i];
        int j = i - 1;
        while (j >= 0) {
            comparaciones++;
            if (arr[j].veces > key.veces) {
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

int main() {
    // RETO 1
    // Se selecciona la lista de clase, pero ya ordenada
    int n = 8;
    int datosBubble1[] = {11, 12, 22, 25, 33, 45, 64, 90};
    int datosBubble2[] = {11, 12, 22, 25, 33, 45, 64, 90};
    int datosInsertion[] = {11, 12, 22, 25, 33, 45, 64, 90};

    bubbleSinBandera(datosBubble1, n);
    cout << "Bubble sin bandera: " << cambios << " cambios y " << comparaciones << " comparaciones.\n";

    bubbleSort(datosBubble2, n);
    cout << "Bubble con bandera: " << cambios << " cambios y " << comparaciones << " comparaciones.\n";

    insertionSort(datosInsertion, n);
    cout << "Insertion sort: " << cambios << " cambios y " << comparaciones << " comparaciones.\n";

    // RETO 2
    // Los registros del proyecto: (veces prestado, codigo del equipo)
    int N = 20;
    Equipo registros[20] = {
        {14, "EQ-01"}, {3, "EQ-02"},  {27, "EQ-03"}, {9, "EQ-04"},  {21, "EQ-05"},
        {5, "EQ-06"},  {18, "EQ-07"}, {30, "EQ-08"}, {3, "EQ-09"},  {12, "EQ-10"},
        {25, "EQ-11"}, {7, "EQ-12"},  {16, "EQ-13"}, {22, "EQ-14"}, {9, "EQ-15"},
        {29, "EQ-16"}, {10, "EQ-17"}, {19, "EQ-18"}, {2, "EQ-19"},  {24, "EQ-20"}
    };

    // Se copian los registros para no perder los originales
    Equipo registrosBubble[20];
    for (int i = 0; i < N; i++) registrosBubble[i] = registros[i];
    bubbleSort(registrosBubble, N);
    cout << "\nRegistros ordenados por veces prestado:\n";
    for (int i = 0; i < N; i++) {
        cout << registrosBubble[i].codigo << " -> " << registrosBubble[i].veces << " veces prestado\n";
    }

    // RETO 3
    // Cada método trabaja con su propia copia de los registros
    Equipo registrosSelection[20];
    Equipo registrosInsertion[20];
    for (int i = 0; i < N; i++) {
        registrosBubble[i] = registros[i];
        registrosSelection[i] = registros[i];
        registrosInsertion[i] = registros[i];
    }

    bubbleSort(registrosBubble, N);
    int cambiosB = cambios, comparacionesB = comparaciones;
    selectionSort(registrosSelection, N);
    int cambiosS = cambios, comparacionesS = comparaciones;
    insertionSort(registrosInsertion, N);
    int cambiosI = cambios, comparacionesI = comparaciones;

    cout << "\nMetodo          | Comparaciones | Intercambios |\n";
    cout << "BubbleSort      | " << comparacionesB << "          | " << cambiosB << "        |\n";
    cout << "SelectionSort   | " << comparacionesS << "          | " << cambiosS << "        |\n";
    cout << "InsertionSort   | " << comparacionesI << "          | " << cambiosI << "        |\n";

    return 0;
}

/*
 RETO 1: bandera en Bubble

 Se agrego la variable swapped: empieza en false en cada pasada y si hubo un intercambio
 pasa a true. Si al terminar la pasada sigue en false la lista ya esta ordenada y se corta con break.
 Sobre los 8 datos ya ordenados:
   Bubble sin bandera: 28 comparaciones
   Bubble con bandera: 7 comparaciones (una sola pasada)
   Insertion sort: 7 comparaciones
 Baja de 28 a 7, igual que Insertion.
 (en insertionSort se cuenta tambien la comparacion que falla y corta el while, si no
 se contara daria 0 en una lista ordenada)

 RETO 2: registros por veces prestado

 Cada registro es un struct Equipo con las veces prestado y el codigo. Como no se usa template,
 los metodos tienen una version para int (Reto 1) y otra para Equipo (Reto 2 y 3) que es igual
 pero compara arr[j].veces. Queda de menor a mayor. Para cambiar los datos solo se edita el
 arreglo registros.

 RETO 3: tabla de comparaciones e intercambios con los 20 registros

 Metodo          | Comparaciones | Intercambios |
 BubbleSort      | 190           | 88           |
 SelectionSort   | 190           | 19           |
 InsertionSort   | 105           | 19           |

 Selection siempre hace las mismas comparaciones (n*(n-1)/2 = 190) sin importar el orden de los datos.
 Bubble es la que mas intercambios hace y Selection e Insertion son las que menos.
*/
