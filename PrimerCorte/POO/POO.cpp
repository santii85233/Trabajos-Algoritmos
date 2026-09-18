#include <iostream>


using namespace std;

//Se inicializa con class y el nombre en Mayuscula
class Nodo{
    int dato;
    Nodo* siguiente;    //se ayuda el puntero para iniciar o borrar memoria; se utiliza -> para poder acceder al puntero

    //Metodo constructor (Se llama igual que la clase y se genera vacio)
    Nodo(int valor), dato(valor), siguiente(nullptr){}

}

int main(){

    Nodo* cabeza = new Nodo(10);    //se crea el objeto 1
    cabeza->siguiente = new Nodo(20); //Se crea el segundo enlazado al primero

    cout<<cabeza->dato<<endl;   //10
    cout<<cabeza->siguiente->dato<<endl;    //20

    delete cabeza;
    delete cabeza->siguiente;
    return 0;

}