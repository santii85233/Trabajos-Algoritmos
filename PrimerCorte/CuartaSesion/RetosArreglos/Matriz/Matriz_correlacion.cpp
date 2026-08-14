#include <iostream>

using namespace std;

int main(){
    int matrizSemaforo[3][3]={{1,4,7},{2,5,8},{3,6,9}};
    for(int f=0;f<3;f++){
        for(int c=0;c<3;c++){
            cout<<"["<<matrizSemaforo[f][c]<<"]"<<"\t";
        }
        cout<<endl;
    }
}