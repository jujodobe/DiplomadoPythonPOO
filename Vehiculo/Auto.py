# Esto es la subclase o clase Hija
from Vehiculo import Vehiculo

class Auto(Vehiculo):

  def __init__(self, chapa, modelo, año, funciona, marca, color, encendido, capacidadValija):
    super().__init__(chapa, modelo, año, funciona, marca, color, encendido)
    self.__capacidadValija = capacidadValija

  def getCapacidadValija(self):
    return self.__capacidadValija

  def setCapacidadValija(self, capacidadValija):
    self.__capacidadValija = capacidadValija

  def Arrancar(self):
    #Logica de programacion del encendido
    if self.__funciona == True:
      print('Auto encendido...')
      self.__encendido = True
    else:
      print('Auto no funciona')
      self.__encendido = False

  def apagarAuto(self):
    if self.__encendido == True:
      print('Apangado auto...')
      print('Auto Apagado')
      self.__encendido = False
    else:
      print('El auto está apagado...')