#include <iostream>

using namespace std;

int main(){

    //Declarar filas y columnas
    int columnas = 3, filas = 2;

    //Crear matriz con el tamaño anterior
    int matrizMapa[filas][columnas] = {{1, 2, 3},
                                       {4, 5, 6}};

    // Crear matriz invertida para guardar el resultado
    int matriz[columnas][filas];
    

    // Recorrer cada una de las columnas de la matriz original
    for(int i = 0; i < columnas; i++){
        
        // Recorrer cada una de las filas de la matriz original
        for(int j = 0; j < filas; j++){
            
            //Guardar el valor inverso en una variable
            int valor = matrizMapa[filas - 1 - j][i];
            
            // darle el valor a la posicion inversa de la matriz
            matriz[i][j] = valor;
        }
    }

//For para imprimir la matriz volteada
for(int f = 0; f < columnas; f++){
    for(int c = 0; c < filas; c++){
        cout << "[" << matriz[f][c] << "]" << " ";
    }
    cout << endl;
}
return 0;

}
