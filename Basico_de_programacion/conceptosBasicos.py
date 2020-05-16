print('hola')
def my_first_function():
    return "Hello World!"
print (my_first_function())

class Estudiante(object):
  def __init__(self,nombre_r,edad_r):
      self.nombre = nombre_r
      self.edad = edad_r

  def hola(self):
  	return "Mi nombre es %s y tengo %i" % (self.nombre, self.edad)
e = Estudiante("Arturo", 21)
print (e.hola())
for i in range(10):
    print (i)
x = 0
while (x < 10):
     print (x)
     x += 1
