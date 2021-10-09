"""Esta aplicación debe entregar la posibilidad de iniciar sesión con un perfil individual.
Generalmente, uno ingresa a su cuenta personal en una página, ésta te saluda y te reconoce"""

usuario = input ("BIENVENIDO POR FAVOR INGRESE SU USUARIO ")

if usuario == "neifer":
        contraseña = input("ingrese la contraseña: ")
        if contraseña == "123456":
            print("BIENVENIDO", usuario, "A ESTA MARAVILLOSA PAGINA")
        else:
            print("la contraseña es incorrecta")
else:
        print("el usuario no esta en la base de datos")

#-------------------------------------------------------------------------------------------------#

""""Crea un string con el nombre de al menos 7 usuarios de tu aplicación."""
"""Convierte tu string en una lista, en la cual cada elemento es un usuario"""

lista_nombres = []

while len(lista_nombres) <= 6:
    nombre = input('para iniciar, por favor digita tu nombre completo')
    lista_nombres.append(nombre)
    print(lista_nombres)
print('Usuarios registrados')

#--------------------------------------------------------------------------------------------------#

""""Imprima en pantalla la cantidad usuarios que tiene tu aplicación."""

print(lista_nombres)
print('La cantidad de usuarios son:', len(lista_nombres))

#--------------------------------------------------------------------------------------------------#

"""Ahora piensa en tres de ellos. Búscalos en la lista con el método adecuado."""

print('ESTOS 3 USUARIOS GANARON UN PREMIO')
print(lista_nombres[1])
print(lista_nombres[3])
print(lista_nombres[6])

#----------------------------------------------------------------------------------------------------#

"""Imprima en pantalla un mensaje de saludo a los diferentes usuarios. ¿Qué técnica puedes utilizar
para realizar esto?
"""

for i in lista_nombres:
    print("HOLA", i ,"BIENVENIDO A TU SESION")
    i =+ 1


