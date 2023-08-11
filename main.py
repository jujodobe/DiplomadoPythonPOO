from Personas.Clientes import Cliente
from Personas.Funcionarios import Funcionario

Pedro = Funcionario("Pedrito", "123", "123123", "Pedro", "Garcia", "0912312312", 19, "Mail@example")
Mario = Cliente("Mario", "10-08-2023", "1233546", "Mario", "Gomez", "098323232", 15, "Mail@example.com")

print(f'Usuario: { Pedro.getUsuario() }, Password: {Pedro.getPassword()}')
print(f'Cliente: {Mario.getNombre()}, Fecha Ingreso: {Mario.getFechaIngreso()} y {Mario.esMayorDeEdad()}')

print("INFORMACIONES DE LAS PERSONAS")

print(Pedro.verInformacion())
print(Mario.verInformacion())







def comentario():
      '''
      v_auto = Auto('VFE-764', 'Fortuner', 2010, True, 'Toyota', '', False, 'Grande')
      v_moto = Moto('HFJ-012', 'Dakar', 2016, True, 'Kenton', 'Azul', False, 250)
      
      
      v_auto.setChapa('JHF-005')
      
      print('DATOS DEL AUTO')
      print(v_auto.getChapa())
      print(f'El vehiculo es de la marca {v_auto.getMarca()} '
            f'y el modelo es {v_auto.getModelo()}')
      print(f'La capacidad del maletero tiene un tamaño {v_auto.getCapacidadValija()}')
      
      print()
      print()
      
      print('DATOS DE LA MOTO')
      print(f'La moto es de la marca {v_moto.getMarca()} del año {v_moto.getAño()}')
      print(f'El tamaño en cilidrada de esta moto es de {v_moto.getCilindrada()}')
      
      
      '''

