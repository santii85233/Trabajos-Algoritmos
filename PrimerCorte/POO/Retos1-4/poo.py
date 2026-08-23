"""
Teniendo en cuenta los conceptos vistos, cree la siguiente estructura:
Defina el Paquete Salud, dentro de él cree la Clase Persona y defina los atributos tipoDoc, documento, nombre, apellido, 
peso, estatura, edad, sexo y los 

métodos:
pedirDatos()→ que solicite los datos de la persona
mostrarPersona(
) imprime los datos ingresados
calcularlmc()→Primero se calcula
pesoActual-peso(en kg)/(estatura(en m)^2
Si resultado menor menor que 20, "el peso está por debajo de lo ideal",
Si devuelve un número entre 20 y 25 (incluidos), "el peso es ideal" y
Si devuelve un valor mayor que 25 significa que tiene sobrepeso
mayorEdad()→ Determinar si es mayor de edad o no

"""

# Definición de la clase Persona para gestionar datos de salud
class Persona():
    def __init__(self):
        # Inicialización de atributos personales con valores por defecto
        self.tipoDoc = 0
        self.documento = 0
        self.nombre = ""
        self.apellido = ""
        self.peso = 0
        self.estatura = 0
        self.edad = 0
        self.sexo = ""
        
    # Método para solicitar los datos
    def pedirDatos(self):
        print("\n--- DATOS PERSONA ---")
        print("Ingrese el siguiente numero si su tipo de documento es:")
        print("1.CC.")
        print("2.TI.")
        print("3.Pasaporte.")
        print("4.Otro.")
        self.tipoDoc = int(input("Ingrese el tipo de documento: "))
        self.documento = int(input("Ingrese el número de documento: "))
        self.nombre = input("Ingrese el nombre: ")
        self.apellido = input("Ingrese el apellido: ")
        self.peso = float(input("Ingrese el peso en kg: "))
        self.estatura = float(input("Ingrese la estatura en metros: "))
        self.edad = int(input("Ingrese la edad: "))
        self.sexo = input("Ingrese el sexo (M/F): ")

    # Método para convertir el número de tipo de documento a su equivalente en texto
    def tipoDato(self):
        if self.tipoDoc==1:
            tipoDato="CC"
            return tipoDato
        if self.tipoDoc==2:
            tipoDato="TI"
            return tipoDato
        if self.tipoDoc==3:
            tipoDato="Pasaporte"
            return tipoDato
        if self.tipoDoc==4:
            tipoDato="Otro"
            return tipoDato
            
    # Método para imprimir los datos de la persona
    def mostrarPersona(self):
        print("--- DATOS DE LA PERSONA ---")
        print(f"Tipo de Documento: {self.tipoDato()}")
        print(f"Número de Documento: {self.documento}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Peso: {self.peso} kg")
        print(f"Estatura: {self.estatura} m")
        print(f"Edad: {self.edad} años")
        print(f"Sexo: {self.sexo}")

    # Método para calcular el IMC y mostrar según el resultado
    def calcularIMC(self):
        imc = self.peso / (self.estatura ** 2)
        if imc < 20:
            print("El peso está por debajo de lo ideal")
        elif 20 <= imc <= 25:
            print("El peso es ideal")
        else:
            print("Tiene sobrepeso")

    # Método para determinar si la persona es mayor de edad
    def mayorEdad(self):
        if self.edad >= 18:
            print( "Es mayor de edad")
        else:
            print("No es mayor de edad")

# Definición de la subclase Empleado que hereda de Persona
class Empleado(Persona):
    def __init__(self):
        # Llamada al constructor de la clase base (Persona)
        super().__init__()

        # Inicialización de atributos propios del empleado
        self.cargo = ""
        self.departamento= ""
        self.valorHora = 0
        self.horastrabajas = 0
        
    # Metodo para solicitar datos personales (heredados) y laborales
    def pedirDatosEmpleado(self):
        super().pedirDatos()
        print("\n--- DATOS LABORALES ---")
        self.cargo = input("Ingrese el cargo: ")
        self.departamento = input("Ingrese el departamento: ")
        self.valorHora = float(input("Ingrese el valor por hora: "))
        self.horasTrabajadas = float(input("Ingrese las horas trabajadas: "))
        
    # Metodo para calcular la liquidación de honorarios
    def calcularHonorarios(self):
        self.valorTotal = self.valorHora * self.horasTrabajadas
        self.reteica = self.valorTotal * (0.966/100)
        totalAPagar = self.valorTotal - self.reteica
        print("\n--- DETALLE DEL EMPLEADO Y HONORARIOS ---")
        print("Tipo de Documento: " , self.tipoDato())
        print("Número de Documento: " , self.documento)
        print("Nombres: " , self.nombre)
        print("Apellidos: " , self.apellido)
        print("Cargo: " , self.cargo)
        print("Departamento: " , self.departamento)
        print("Horas Trabajadas: " , self.horasTrabajadas)
        print("Valor por Hora: $" , self.valorHora)
        print("Total a Pagar (Menos RETEICA 0.966%): $" , totalAPagar)

# ejecución de los métodos
emp= Empleado()
emp.pedirDatosEmpleado()
emp.mostrarPersona()
emp.calcularIMC()
emp.mayorEdad()
emp.calcularHonorarios()