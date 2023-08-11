from Personas.Persona import Persona


class Cliente(Persona):
    def __init__(self, estado, fechaIngreso, cedula, nombre, apellido, celular, edad, mail):
        super().__init__(cedula, nombre, apellido, celular, edad, mail)
        self.__estado = estado
        self.__fechaIngreso = fechaIngreso


    def getEstado(self):
        return self.__estado

    def getFechaIngreso(self):
        return self.__fechaIngreso