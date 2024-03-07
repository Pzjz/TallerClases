class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")

class Salario:
    def __init__(self):
        self.salario = float(input("Ingrese el salario del empleado: "))

class Designacion(Empleado, Salario):
    def __init__(self):
        Empleado.__init__(self)
        Salario.__init__(self)

    def asignar_cargo(self):
        cargo = input("Ingrese el cargo del empleado: ")
        self.cargo = cargo
        print(f"El empleado {self.nombre} con salario {self.salario} ha sido designado como {self.cargo}")

empleado_designado = Designacion()
empleado_designado.asignar_cargo()