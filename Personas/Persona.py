class Persona:
    def __init__(self, cedula, nombre, apellido, celular, edad, mail):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__celular = celular
        self.__edad = edad
        self.__mail = mail

    def esMayorDeEdad(self):
        if(self.__edad >= 18):
            return "Es mayor de edad"
        else:
            return "Es menor de edad"

    def verInformacion(self):
        return f'Nombre: {self.__nombre}, ' \
               f'Apellido: {self.__apellido},' \
               f'Cedula: {self.__cedula}, ' \
               f'Celular: {self.__celular},' \
               f'Edad: {self.__edad},' \
               f'Mail: {self.__mail}'

    def getCedula(self):
        return self.__cedula

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getCelular(self):
        return self.__celular

    def getEdad(self):
        return self.__edad

    def getMail(self):
        return self.__mail