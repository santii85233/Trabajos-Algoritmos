#include <iostream>
#include <string>

using namespace std;

int main() {
    int dias=5; //dias de la semana
    int franjas=6; // total de franjas
    int matrizMonitorias[franjas][dias] = {{2,4,6,12,4}, //"08:00 am- 10:00 am"
                  {1,5,2,11,2}, //10:00 am- 12:00 pm
                  {3,4,5,7,1},  //12:00 pm- 1:00 pm
                  {0,2,0,0,0},  //3:00 pm- 4:00 pm
                  {0,4,6,9,5},  //4:00 pm- 5:00 pm
                  {0,0,0,0,4}}; //5:00 pm- 6:00 pm

    string semana[dias]={"Lunes","Martes","Miercoles","Jueves","Viernes"};
    string franjash[franjas]={"08:00 am- 10:00 am","10:00 am- 12:00 pm","12:00 pm- 1:00 pm","3:00 pm- 4:00 pm","4:00 pm- 5:00 pm","5:00 pm- 6:00 pm"};



    int totalesFranja[franjas]={0}; // Lista para guardar la suma total de personas por franja
    int totalesDia[dias]={0}; // Lista para guardar la suma total de personas por dia
    int totalDia =0; //Entero para guardar la cantidad total de personas por dia
    int totalFranja=0; //Entero para guardar la cantidad de personas por franja
    int maximo=0; // maximo de personas por franja y por dia 
    int dia, hora;
    int indice=0;
for (int i=0;i<franjas;i++){
    for(int j=0;j<dias;j++){
        //Analiza si esa posición es el maximo de personas en una franja
        if(matrizMonitorias[i][j] >maximo){
            maximo= matrizMonitorias[i][j];
            dia= j;
            hora= i;
        }
        //Hace la suma de personas por franja
        totalFranja+=matrizMonitorias[i][j];
    }
    totalesFranja[indice]= totalFranja;
    totalFranja=0;
    indice +=1;
}
//Hace la suma de cada columna de cada fila es decir el recuento de personas por dia

for(int c=0; c<dias;c++){
    for(int f =0;f<franjas;f++){

        // Se hace el recuento del total de personas por dia
        totalDia +=matrizMonitorias[f][c];
    }

    //Se agregan a una lista y se reinicia para el siguiente dia
    totalesDia[c]= totalDia;
    totalDia = 0;
} 
cout<<"El dia con más asistentes fue el "<<semana[dia]<<" En la franja "<<franjash[hora]<<" con un total de "<<maximo<<" personas."<<endl;
//Se reinicia para ser usada para analizar el maximo de personas por dia 
int maximoFranja=0;

//Se recorre la lista de la suma de los dias y se encuentra al mayor y se almacena
for(int x=0;x<dias;x++){
    
    if (totalesDia[x] >maximoFranja){
        maximoFranja=totalesDia[x];
        indice=x;
    }
}
cout<<"El dia con más personas en total, fue el "<<semana[indice]<<", contando con un total de "<<maximoFranja<<" Personas."<<endl;

maximo = 0; 

//Se identifica que franja tiene menos de 5 personas y se imprime 
for(int x=0;x<franjas;x++){
    if (totalesFranja[x] <5){
        maximo=totalesFranja[x];
        indice=x;
        cout<<"La franja "<<franjash[indice]<<" se encuentra por debajo de 5 personas de asistencia, contando con "<<maximo<<" personas."<<endl;
    }
}
return 0;

}
