#include <iostream>
#include <cstdlib>  //Libreria generar numero random
#include <thread>   //Libreria agrega delay
#include <chrono>   //Libreria manejo tiempo en segundos
#include <string>   //Libreria strings

using namespace std;
using namespace std::this_thread; // para no tener que escribir this_thread:: antes de sleep_for()
using namespace std::chrono;      // para no tener que escribir chrono:: antes de seconds()
//prueba
int main() {

    float compra, descuento, valorFinal;
    int bolita;
    string enter;

    cout << "==========================================" << endl;
    cout << "  Bienvenido a Supermercados Noe" << endl;
    cout << "  Promocion de Aniversario" << endl;
    cout << "==========================================" << endl;
    cout << "Ingrese el valor de su compra: ";
    cin >> compra;

    if (compra <= 50000) {
        cout << "Lo sentimos, tu compra debe ser mayor a 50.000 para participar en la promocion." << endl;
    } else {
        cout << "¡Girando la esfera de bolitas!" << endl;

        //Simulación del sorteo
        cout << "..." << endl;
        sleep_for(seconds(1));
        cout << "..." << endl;
        sleep_for(seconds(1));
        cout << "..." << endl;
        sleep_for(seconds(1));

        cout << "¡Tu bolita ha salido!" << endl;

        bolita = rand() % 4 + 1; //Genera un numero random del 1 al 4

        //Dice el color de la bolita y el porcentaje de descuento
        if (bolita == 1) {
            cout << "¡¡Ha salido la bolita ROJA!!" << endl;
            descuento = 0.10;
        }
        if (bolita == 2) {
            cout << "¡¡Ha salido la bolita AZUL!!" << endl;
            descuento = 0.30;
        }
        if (bolita == 3) {
            cout << "¡¡Ha salido la bolita AMARILLA!!" << endl;
            descuento = 0.50;
        }
        if (bolita == 4) {
            cout << "¡¡Ha salido la bolita BLANCA!!" << endl;
            descuento = 1.00;
        }

        valorFinal = compra - (compra * descuento);

        //Muestra el resultado al cliente
        cout << "Descuento obtenido: " << (descuento * 100) << "%" << endl;
        cout << "Valor de tu compra: $" << compra << endl;

        if (descuento == 1.00) {
            cout << "¡Felicidades! Tu compra es GRATIS." << endl;
            cout << "Valor final a pagar: $0" << endl;
        } else {
            cout << "Valor final a pagar: $" << valorFinal << endl;
        }
    }

    return 0;
}