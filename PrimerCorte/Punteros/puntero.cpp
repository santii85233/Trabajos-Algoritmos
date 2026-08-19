#include <iostream>

using namespace std;

    void porValor(int a, int b){
        int t=a;
        a=b;
        b=t;
    };
    void porRetorno(int* a, int* b){
        int t = *a;
        *a=*b;
        *b=t;
    };
    void porReferencia(int& a, int&b){
        int& t= a;
        a = b;
        b = t;
    };
    

int main(){
    int x=10;

    int* p= &x;    //'*' trae el dato del tipo mencionado
                   //'&' pide la dirección de donde este la variable

    cout<<p<<endl; //imprime la direccion en memoria
    cout<<*p<<endl; //imprime el valor que hay en la direccion de p

    //si por ejemplo se modifica x; el apuntador seguiria estando en el valor anterior

    *p = 99; //se modifica x atraves de p 


    cout<< x;



    

}