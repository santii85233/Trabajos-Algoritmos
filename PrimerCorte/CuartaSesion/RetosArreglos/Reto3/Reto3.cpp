#include <iostream>

using namespace std;

int main(){
    bool prueba;
    int palindromo[5] ={1, 5, 9, 5, 1};
    int inicio = 0;
        while(inicio<5){
            if(palindromo[inicio]!=palindromo[5-(inicio+1)]){
                prueba=false;
                break;
            }
            inicio +=1;
            prueba =true;
        }
        if (prueba){
            cout<<"El codigo ingresado es válido."<<endl;
        }else{
            cout<<"El codigo ingresado es invalido."<<endl;
        }
    return 0;
}
/*
int main(){
    bool prueba;
    int inicio, N;
    inicio = 0;
    cout<<"Ingrese la cantidad de numeros del codigo a ingresar:";
    cin>>N;
    int palindromo[N];
    if (N > 0){
        for (int i=0; i<N;i++){
            cout<<"Ingrese el valor "<<i+1<< " de su medición:";
            cin>>palindromo[i];
        }
    }
        while(inicio<N){
            if(palindromo[inicio]!=palindromo[N-(inicio+1)]){
                prueba=false;
                break;
            }
            inicio +=1;
            prueba =true;
        }
        if (prueba){
            cout<<"El codigo ingresado es válido."<<endl;
        }else{
            cout<<"El codigo ingresado es invalido."<<endl;
        }
    return 0;
}*/
