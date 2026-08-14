#include <iostream>

using namespace std;

int main(){
    int rachaActual, mejorRacha;
    int lluvias[9]={0,1,1,0,1,1,1,0,1};
    rachaActual= 0;
    for(int i=0;i<9;i++){
        if (lluvias[i]==1){
            rachaActual +=1;
        }
        if(lluvias[i]==0){
            mejorRacha =rachaActual;
            rachaActual =0;
        }
    }
    cout<<"La mayor racha alcanzada de dias de lluvias fue de "<<mejorRacha<<" dias."<<endl;
    return 0;
}