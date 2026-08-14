#include <iostream>

using namespace std;

int main(){
int valor, N, descartados, suma, valido, error;
float promedio;
error = -999;
suma = 0;
valido = 0;
descartados = 0;
promedio =0;

cout<<"Ingrese la cantidad de temperaturas a ingresar:";
cin>>N;
int Temperaturas[N];
if (N > 0){
    for (int i=0; i<N;i++){
        cout<<"Ingrese el valor "<<i+1<< " de su medición:";
        cin>>Temperaturas[i];
    }
        for(int t=0; t<N;t++){
            if (Temperaturas[t] != error){
                suma += Temperaturas[t];
                valido += 1;
            }
            else{
                descartados +=1;
            }
        }
        promedio= (float)suma/valido;

    cout<<"Promedio:"<<promedio<<endl;
    cout<<"Valores Correctos:"<<valido<<endl;
    cout<<"Valores invalidos:"<<descartados<<endl;
}
else{
    cout<<"Ingrese un valor válido"; 
}
    return 0;
}   