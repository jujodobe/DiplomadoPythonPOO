from Vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, chapa, modelo, año, funciona, marca, color, encendido, cilindrada):
        super().__init__(chapa, modelo, año, funciona, marca, color, encendido)
        self.__cilindrada = cilindrada

    def getCilindrada(self):
        return self.__cilindrada

    def setCilindrada(self, cilindrada):
        self.__cilindrada = cilindrada
