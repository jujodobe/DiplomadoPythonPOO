from Vehiculo import Vehiculo
class Auto(Vehiculo):

  def __init__(self):
    self.__chapa = ''
    self.__modelo = ''
    self.__año = 0
    self.__funciona = True
    self.__marca = ''
    self.__color = ''
    self.__encendido = False
    self.__tamaño = 'grande'

  # Metodo que fucniona para retornar el valor del atributo chapa de la clase
  def getChapa(self):
      ruedas = 4
      return self.__chapa #Retorna el valor de chapa

  def setChapa(self, chapa):
    self.__chapa = chapa

  def getModelo(self):
    return self.__modelo

  def setModelo(self, modelo):
    self.__modelo = modelo



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