"""
Sistema de Gestión de Notas
=======================================
Programa CLI para registro, observación y edición de notás de estudiantes.
Desarrollado con enfoque educativo para demostrar:
- Modularización de código
- Manejo de estructuras de datos
- Validación de entradas
- Programación estructurada
- Documentación técnica

Autor: Alejandro Rojas
Fecha: [12/02/25]

Estructura del programa:
1. Definición de tipos de datos
2. Funciones especializadas
3. Menú interactivo
4. Flujo principal de ejecución
"""

#Definicion de variables utilizadas


estudiantes = [] #Lista de estudiantes que estan matriculados
notas_estudiantes = {} #Diccionario para almacenar notas de estudiantes junto con su nombre 

def continuar(): #funcion que utilizo para que el usuario de enter y generar pausas y diviciones de codigo 
    """
    Pausa en la ejecución del programa para que el usuario pueda leer y de enter"
    """
    input("PRECIONA ENTER PARA CONTINUAR \n")
    return

def nombre(): # funcion para obtener el nombre del estudiante y retornarlo cuando se necesite
    """
    funcion para obtener el nombre del estudiante y retornarlo
    """
    estudi = input("NOMBRE DEL ESTUDIANTE:  \n").upper()
    if estudi == str:
        print("INGRESE UN NOMBRE VALIDO")
        nombre()
    return estudi

def inicio(): #El inicio basico del codigo, solo aparece una vez al iniciar el programa
    """
    El inicio del programa, como pantalla de carga
    """
    print("""
    --------------------
    ---SOFTWARE NOTAS---
    --------------------
          """)
    continuar()
    menu()

#El menu principal del sistema, donde se interactua con el usuario

def menu():
    """
    El menu principal del codigo, donde se interactua para utilizar diferentes funciones
    """
    print("""
    ---------------
    -----MENU------
    ---------------
    """)
    # dependiendo de op, se entra o no a los diferentes condicionales con sus respectivas funciones
    op = int(input("""
    1. INSERTAR NOTAS
    2. VER NOTAS DE ESTUDIANTE
    3. EDITAR NOTAS DE ESTUDIANTE
    4. SALIR 
                 
    ESCRIBE LA OPCION QUE DECEE EJECUTAR
    """))
    if  op == 1:
        #agregar notas
        notas()
    elif op == 2:
        #ver las notas de x estudiante
        ver_notas()
    elif op == 3:
        #editar las notas de un estudiante 
        editar_nota()
        # salida del sistema
    elif op == 4:
        print()
        print("**GRACIAS POR USAR EL SOFTWARE**")
        print()
        continuar()
        #opcion no valida como str o float
    else:
        print("***OPCION INCORRECTA***")
        #volver al menu
        menu()

#funcion para agregar las notas
def notas():
    """
    Funcion para agregar notas, esta funcion diferencia entre usuarios nuevos y usuarios ya registrados,
    """
    print()
    #se pide nombre de estudiante
    estudi = nombre()
    #se agrega a la lista de estudaintes si no esta en ella
    if estudi not in estudiantes:
        estudiantes.append(estudi)
    #se pregunta la cantidad de notas a ingresar
    try: 
        agregar_nota = int(input("CUANTAS NOTAS VAS A INGRESAR \n"))
    except:
        print("INGRESE UN NUMERO")
        continuar()
        notas()
    #se crea un bucle el cual añadira las notas al diccionario con la lsita del estudiante 
    for i in range(1, agregar_nota + 1):
        nota = float(input(f" INGRESE LA NOTA {i} DE {estudi} \n"))
        # si el estudiante esta en el diccionario solo se le añade la nota
        if estudi in notas_estudiantes:
            notas_estudiantes[estudi].append(nota)
        #si no esta se crea la lista con las notas
        else:
            lista_notas = []
            #crea la clave con el nombre del estudiante y el valor con la lista de notas
            notas_estudiantes[estudi] = lista_notas
            #se añade la nota a la lista
            notas_estudiantes[estudi].append(nota)
    print(notas_estudiantes)
    continuar()
    #volver al menu 
    menu()
    
#funcion para ver las notas de un estudiante
def ver_notas():
    """
    Funcion pra ver las notas de x estudiante
    """
    print()
    #se pide el nombre del estudiante
    estudi = nombre()
    # si el estudiante esta en la lista de registrados aparece su nota
    if estudi in estudiantes:
        print(f"***LAS NOTAS DEL ESTUDIANTE {estudi} SON : ***")
        print(notas_estudiantes[estudi])
        print()
    #si no esta en la lista de registrados aparece un mensaje
    else:
        print("ESTE ESTUDIANTE NO EXISTE")
        print("-------------------------")
        print("LOS ESTUDIANTES SON: ")
        print(estudiantes)
    continuar()
    #volver al menu
    menu()
# funcion para editar las notas de un estudiante
def editar_nota():
    """
    Funcion para ver las notas de x estudiante 
    """
    print()
    #se pide nombre del estudiante 
    estudi = nombre()
    # se muestran las notas del estudiante para ser editadas
    print(F"**EL ESTUDIANTE TIENE LAS SIGUIENTES NOTAS**")
    print(notas_estudiantes[estudi])
    try:
        #se pide cuantos cambios va a realizar
        cutos_cambios = int(input("CUANTOS CAMBIOS VAS A REALIZAR \n"))
        #bucle para esos cambios 
        for i in range(1, cutos_cambios + 1):
            print(f"**CAMBIO {i}**")
            #se solicita la posicion de la nota para cambiarla
            cambio = int((input("**QUE POSCISION DE LA NOTA QUIERES EDITAR** \n")))
            #se solicita la nueva nota
            nota = float(input("QUE NOTA QUIERES INSERTAR \n"))
            # en la posicison solicitada(-1 ya que en python empiza desde 0 )se inserta la nueva nota
            notas_estudiantes[estudi][cambio - 1] = nota
            print("**CAMBIO REALIZADO**")
            #se muestra el cambio realizado
            print(notas_estudiantes[estudi])
            continuar()
        #volver al menu
        menu()
    except:
        print("INGRESE UN NUMERO")
        continuar()
        editar_nota()



try:
    inicio()
except:
    print("INGRESE UN NUMERO")
    continuar()
    menu()