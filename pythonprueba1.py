# organizacion de empleados enpytho. Primero se crea una clase Empleados que con
# En este caso la relación es así:

       # self = objetos de la clase (este caso empleado1, empleado2,etc)
       # nombre = nombre del empleado (se le asigna al "self" que se indique)
       #






class Empleados:
	def __init__(self, nombre, apellido, sueldo):
		self.nombre = nombre
		self.apellido = apellido
		self.sueldo = sueldo
		self.correo = nombre + '.'+apellido + '@gmail.com'

	def fullname(self):
		return self.nombre + self.apellido

empleado1 = Empleados('Pedro', 'Porras', 14000)
empleado2 = Empleados('Miguel', 'Ayala', 2000)
empleado3 = Empleados('Toño', 'Villa', 15000)
empleado4 = Empleados('Too', 'Villa', 15000)
print(empleado1.fullname())
print(empleado2.__dict__)
print(Empleados.__dict__)
print(Empleado3.__dict__)
