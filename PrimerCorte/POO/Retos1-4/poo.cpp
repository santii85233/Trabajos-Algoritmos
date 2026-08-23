#include <iostream>
#include <string>

using namespace std;

    class Persona {
    private:
        int edad, tipoDoc;
        float peso, estatura;
        string nombre, apellido, sexo, doc;

    public:
        // Constructor de persona 
        Persona() {
            this->tipoDoc = 0;
            this->doc = "";
            this->nombre = "";
            this->apellido = "";
            this->peso = 0.0f;
            this->estatura = 0.0f;
            this->edad = 0;
            this->sexo = "";
        }
        //imprime los detalles 
        void pedirDatos() {
            cout << "\n--- REGISTRO DE DATOS PERSONALES ---" << endl;
            cout << "1. CC\n2. TI\n3. Pasaporte\n4. Otro" << endl;
            cout << "Seleccione el tipo de documento (1-4): ";
            cin >> tipoDoc;
            cout << "Ingrese el numero de documento: ";
            cin >> doc;
            cout << "Ingrese el nombre: ";
            cin >> nombre;
            cout << "Ingrese el apellido: ";
            cin >> apellido;
            cout << "Ingrese el peso en kg: ";
            cin >> peso;
            cout << "Ingrese la estatura en metros (ej: 1.75): ";
            cin >> estatura;
            cout << "Ingrese la edad: ";
            cin >> edad;
            cout << "Ingrese el sexo: ";
            cin >> sexo;
        }
        //retornar que tipo de documento tiene
        string tipoDato() {
            switch (tipoDoc) {
                case 1:  return "CC";
                case 2:  return "TI";
                case 3:  return "PASAPORTE";
                case 4:  return "Otro";
                default: return "DESCONOCIDO";
            }
        }

        //Imprime los datos de la persona
        void mostrarPersona() {
            cout << "\n--- DATOS DE LA PERSONA ---" << endl;
            cout << "Tipo de Documento: " << tipoDato() << endl;
            cout << "Número de Documento: " << doc << endl;
            cout << "Nombre: " << nombre << endl;
            cout << "Apellido: " << apellido << endl;
            cout << "Peso: " << peso << " kg" << endl;
            cout << "Estatura: " << estatura << " m" << endl;
            cout << "Edad: " << edad << " años" << endl;
            cout << "Sexo: " << sexo << endl;
        }

        //Se calcula el IMC
        void calcularIMC() {
            if (estatura <= 0) {
                cout << "Estatura inválida para calcular el IMC." << endl;
                return;
            }
            float imc = peso / (estatura * estatura);
            cout << "IMC: " << imc << " -> ";

            // CORRECCIÓN: En C++ no se puede encadenar '20 <= imc <= 25'
            if (imc < 20) {
                cout << "El peso está por debajo de lo ideal" << endl;
            }
            else if (imc >= 20 && imc <= 25) { 
                cout << "El peso es ideal" << endl;
            }
            else {
                cout << "Tiene sobrepeso" << endl;
            }
        }

        //se verifica si es mayor de edad
        void mayorEdad() {
            if (edad >= 18) {
                cout << "Es mayor de edad" << endl;
            } else {
                cout << "No es mayor de edad" << endl;
            }
        }

        // Getters para que la subclase acceda a los datos
        string getTipoDocumento() { return tipoDato(); }
        string getNumeroDocumento() { return doc; }
        string getNombres() { return nombre; }
        string getApellidos() { return apellido; }
    };

    // Subclase Empleado que hereda de Persona
    class Empleado : public Persona {
    private:
        string cargo, departamento;
        float valorHora, horasTrabajadas;

    public:
        // Constructor con sus campos
        Empleado() : Persona() {
            this->cargo = "";
            this->departamento = "";
            this->valorHora = 0.0f;
            this->horasTrabajadas = 0.0f;
        }


        void pedirDatosEmpleado() {
            // Primero pedimos los datos heredados de Persona
            pedirDatos(); 
            
            // Luego los datos específicos de Empleado
            cout << "\n--- DATOS LABORALES ---" << endl;
            cout << "Ingrese el cargo: ";
            cin.ignore(); // Limpia el buffer de entrada
            getline(cin, cargo);
            cout << "Ingrese el departamento: ";
            getline(cin, departamento);
            cout << "Ingrese el valor por hora: ";
            cin >> valorHora;
            cout << "Ingrese las horas trabajadas: ";
            cin >> horasTrabajadas;
        }

        void calcularHonorarios() {
            float valortotal = (valorHora * horasTrabajadas);
            float reteica = valortotal * (0.966 / 100);
            float totalAPagar = valortotal - reteica;

            cout << "\n--- DETALLE DEL EMPLEADO Y HONORARIOS ---" << endl;
            cout << "Tipo de Documento: " << getTipoDocumento() << endl;
            cout << "Número de Documento: " << getNumeroDocumento() << endl;
            cout << "Nombres: " << getNombres() << endl;
            cout << "Apellidos: " << getApellidos() << endl;
            cout << "Cargo: " << cargo << endl;
            cout << "Departamento: " << departamento << endl;
            cout << "Horas Trabajadas: " << horasTrabajadas << endl;
            cout << "Valor por Hora: $" << valorHora << endl;
            cout << "Total a Pagar (Menos RETEICA 0.966%): $" << totalAPagar << endl;
        }
    };

int main() {
    // Instanciamos el objeto
    Empleado emp;
    
    // Captura de datos completa
    emp.pedirDatosEmpleado();
    

    emp.mostrarPersona();
    emp.calcularIMC();
    emp.mayorEdad();
    
    // metodo de Empleado
    emp.calcularHonorarios();

    return 0;
}

