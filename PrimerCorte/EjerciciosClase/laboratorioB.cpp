#include <iostream>

using namespace std;


int main(){
    int cantidad; 
    double *pesos, suma=0.0;
    cout<<"¿Cuantos puntos de acopio quiere?:";
    cin>>cantidad;

    if (cantidad<0){
        cout<<"La Cantidad ingresada es invalida";
        return 1;
    }
    pesos = new double[cantidad];

    cout<<"Ingrese los pesos de la jornada especial:\n";

    for (double*p = pesos; p< pesos + cantidad; p++){
        cout<<"Pesos:";
        cin>> *p;
    }

    for (double*p = pesos; p< pesos + cantidad; p++){
        suma += *p;
    }

    double promedio = suma / cantidad;
    cout<<"El promedio de los pesos es:"<<promedio<<endl;
    delete[] pesos;

    pesos = nullptr;
    return 0;
}