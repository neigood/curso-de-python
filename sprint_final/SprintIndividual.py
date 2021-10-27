"""SPRINT DE ENTREGA:
Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos durante
el Módulo 1 de Python básico. Por tanto, se debe poner foco en lo siguiente:
● Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu
aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
● Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
● Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe
cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
● Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
● Por cada cuenta debe pedir un número telefónico para contactarse. 
● El programa no terminará de preguntar por los números hasta que todas las organizaciones
tengan un número de contacto asignado.
● El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
● Se debe guardar como un string."""


import  random
import string
import os 
# VARIABLES GLOBALES
Diccionario_usuarios = {} # DICCIONARIO GLOBAL QUE ES CRADO PARA ALMACENAR LOS CLIENTES QUE INGRESEN A LA APLCACIÓN

# FUNCIONES 
#Funcion que limpia la pantalla
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

#Funcion creada para agregar los clientes
def agregaCliente (usuarioDic:dict,contrasena,telefono): # ESTA FUNCION RECIBE COMO PARAMETROS UN DICCIONARIO, UNA CONTRASEÑA Y UN TELEFONO
    datos ={}  
    print('AGREGAR DATOS DEL CLIENTE')
    print('---------------------------')
    print('')    
    nombre = input('Ingrese el nombre: ') 
    contrasena = contrasena 
    telefono = telefono 

#Creamos el diccionario leyendo las variables y asignando los valores
    for variable in ["contrasena","telefono"]:  
        datos[variable] = eval(variable) 
      

#Agregamos el diccionario de datos al diccionario maestro
    print(datos)
    usuarioDic[nombre] = datos # INSERTAMOS AL DICCIONARIO USUARIOSDIC CON CLAVE NOMBRE EL DICCIONARIO DATOS
    print("Bienvenido a ... ")
    print('Cliente Agregado Satisfactoriamente') 
    print(' ')
    continuar = input('Presiona ENTER para continuar.....')
    clearConsole()

    return 'Ha ingresado satisfactoriamente'


# funcion para crear la contraseña de cada usuario
def crear_contrasena(): # Creamos la función crear_contrasena() sin parametros ya que se genera aleatoriamente
    minus = 'qwertyuiopasdfghjklzxcvbnm'
    mayus = minus.upper()
    num = '0123456789'
    base= minus + mayus + num 
    longitud = 10
    muestra = random.sample(base,longitud)
    passw = "".join(muestra)
    return passw 


# funcion para condicionar el ingreso del contacto por parte del usuario
def telefono(): 
    print('PARA INGRESAR A LA APLICACIÓN INGRESE SU NÚMERO DE TELEFONO')
    print('------------------------------') 
    phone = input('Ingresa número telefonico: ')
    while True:
        if len(phone) > 8 or phone == string.ascii_lowercase or phone == string.ascii_uppercase: 
            print('El telefono no puede ser mayor a 8 numeros y no puede contener letras') 
            phone = input('Ingresa número thelefonico: ')
        else:
            print('Contacto ingresado correctamente')
            break
    
    print('')
    print('')      
    continuar = input('Presiona ENTER para continuar.....')
    clearConsole()
    return phone # retornamos la variable phone

# funcion para mostrar los usuarios registrados en la aplicación 
def mostrar_usuarios(Diccionario:dict): 
    print('LISTADO DE CLIENTES EXISTENTES')
    print('------------------------------')         
   #Recorremos la lista de usuarios
    for clave, valor in Diccionario.items(): 
       contrasena = valor['contrasena']
       telefono = valor['telefono'] 
       print(f'Usuario {clave}, posee la siguiente clave: {contrasena} y su telefono de contacto es: {telefono}')
       
    print('')
    print('')      
    continuar = input('Presiona ENTER para continuar.....')
    clearConsole()
    return Diccionario


# INICIO
while True: 
    print("""
    '-------------------------------------------'
    '------------------ MENU -------------------'
    '-------------------------------------------'
    '1. Ingresar a la aplicación'
    '2. Mostrar Usuarios registrados'
    '3. Salir del programa'
    ''
    """)
    opcion = input('Seleccione una opcion---> ')
    print('------------------------------------------')   
    clearConsole()
    if opcion == '1':
        agregaCliente(Diccionario_usuarios,crear_contrasena(),telefono())
        print(Diccionario_usuarios)
    elif opcion == '2':
        mostrar_usuarios(Diccionario_usuarios)
        print(Diccionario_usuarios)
    elif opcion == '3':
        break
    else: 
        print("""
        '--------------------------------'
        'ingrese una opcion correcta: '
        '--------------------------------'
        """)


# FIN