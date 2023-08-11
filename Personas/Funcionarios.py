from Personas.Persona import Persona


class Funcionario(Persona):
    def __init__(self, usuario, password, cedula, nombre, apellido, celular, edad, mail):
        self.__usuario = usuario
        self.__password = password
        super().__init__(cedula, nombre, apellido, celular, edad, mail)

    def verInformacion(self):
       return f'{super().verInformacion()}, usuario: {self.__usuario}, Password: {self.__password}'

    def getUsuario(self):
        return self.__usuario

    def getPassword(self):
        return self.__password