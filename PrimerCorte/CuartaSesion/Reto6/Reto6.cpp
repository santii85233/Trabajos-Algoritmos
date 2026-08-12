#include <iostream>
#include <string>

using namespace std;

int main() {

    int numProductos, cantidad;
    string nombre;
    float precioUno, subtotal, totalCompra, descuento, totalPagar;

    totalCompra = 0;

    cout << "==========================================" << endl;
    cout << "     TIENDA - CALCULO DE COMPRA" << endl;
    cout << "==========================================" << endl;
    cout << "¿Cuantos productos va a comprar?: ";
    cin >> numProductos;

    for (int i = 1; i <= numProductos; i++) {
        cout << endl;
        cout << "--- Producto " << i << " ---" << endl;
        cout << "Nombre del producto: ";
        cin >> nombre;
        cout << "Precio unitario: ";
        cin >> precioUno;
        cout << "Cantidad comprada: ";
        cin >> cantidad;

        subtotal = precioUno * cantidad;
        cout << "Subtotal: $" << subtotal << endl;

        totalCompra += subtotal;
    }

    if (totalCompra > 300000) {
        descuento = totalCompra * 0.10;
    } else if (totalCompra >= 150000 && totalCompra <= 300000) {
        descuento = totalCompra * 0.05;
    } else {
        descuento = 0;
    }

    totalPagar = totalCompra - descuento;

    cout << endl;
    cout << "==========================================" << endl;
    cout << "           RESUMEN DE LA COMPRA" << endl;
    cout << "==========================================" << endl;
    cout << "Total antes del descuento: $" << totalCompra << endl;
    cout << "Descuento aplicado: $" << descuento << endl;
    cout << "Total a pagar: $" << totalPagar << endl;

    return 0;
}