#include <iostream>

using namespace std;

int main(){
    int tamano= 3; //se decide el tamaño de la matriz (no tiene ñ por escalado)
    int matrizCuadrada[tamano][tamano]={{1,2,3},
                                        {4,5,6},
                                        {7,8,9}};     
    int suma1=0; //Se define la suma de las diagonales principales
    int suma2=0; //se define la suma de las diagonales secundarias

    //Se empieza a iterar la matriz 
    for(int i=0;i<tamano;i++){

        // Se saca y suma el indice de la columna a sumar de la secundaria
        int indice=tamano-1-i;
        suma2+=matrizCuadrada[i][indice]; 
        
        //Se iteran las filas junto a las columnas
        for (int j=0;j<tamano;j++){
            
            //verifica que sea la principal
            if(i==j){
                suma1 +=matrizCuadrada[i][j];
            }
        }
    }

//Se comparan para dar acceso
if (suma1==suma2){
    cout<<"Ambas diagonales coinciden, acceso permitido."<<endl;
}else{
    cout<<"Las diagonales no coinciden, acceso prohibido."<<endl;
}
    return 0;
}