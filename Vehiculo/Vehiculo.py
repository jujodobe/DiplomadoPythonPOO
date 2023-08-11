# Esto es la superclase
class Vehiculo:

  def __init__(self, chapa, modelo, año, funciona, marca, color, encendido):
    self.__chapa = chapa
    self.__modelo = modelo
    self.__marca = marca
    self.__año = año
    self.__funciona = funciona
    self.__color = color
    self.__encendido = encendido

  def getChapa(self):
    if self.__chapa != '':
      return self.__chapa
    else:
      return 'No tiene valor'

  def getMarca(self):
    return self.__marca

  def getModelo(self):
    return self.__modelo

  def setChapa(self, chapa):
    self.__chapa = chapa

  def getAño(self):
    return self.__año


