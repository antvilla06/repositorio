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

empleado1 = Empleados('Pedro', 'Porras', 10000)
empleado2 = Empleados('Mike', 'Ayala', 10000)
empleado3 = Empleados('Toño', 'Villa', 15000)

print(empleado1.fullname())
print(empleado2.__dict__)
print(Empleados.__dict__)
