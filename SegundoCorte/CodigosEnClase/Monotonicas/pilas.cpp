#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector<int> siguienteMayor(const vector<int>& a){
    int n = a.size();
    vector<int> result(n, -1);
    stack<int> pila;

    for (int i =0; i<n;i++){
        while(!pila.empty() && a[i]> a[pila.top()]){
            result[pila.top()]=a[i];
            pila.pop();
        }
        pila.push(i);
    }
    return result;
}

int main(){
    vector<int> a={73,74,75,71,69,72,76,73};
    for(int x: siguienteMayor(a)) cout<<x<<" ";
}
