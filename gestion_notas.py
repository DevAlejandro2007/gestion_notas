estudiantes = []
notas_estudiantes = {}

def continuar():
    input("PRECIONA ENTER PARA CONTINUAR")
    return

def nombre():
    estudi = input("NOMBRE DEL ESTUDIANTE AL QUE SE DESEA VER NOTAS \n").upper()
    return estudi

def inicio(): 
    print("""
    --------------------
    ---SOFTWARE NOTAS---
    --------------------
          """)
    continuar()
    menu()

def menu():
    print("""
    ---------------
    -----MENU------
    ---------------
    """)

    op = int(input("""
    1. INSERTAR NOTAS
    2. VER NOTAS DE ESTUDIANTE
    3. EDITAR NOTAS DE ESTUDIANTE
    4. SALIR 
                 
    ESCRIBE LA OPCION QUE DECEE EJECUTAR
    """))
    if  op == 1:
        notas()
    elif op == 2:
        ver_notas()
    elif op == 3:
        editar_nota()
    elif op == 4:
        print()
        print("**GRACIAS POR USAR EL SOFTWARE**")
        print()
        continuar()
    else:
        print("***OPCION INCORRECTA***")
        menu()


def notas():
    print()
    estudi = nombre()
    estudiantes.append(estudi)
    agregar_nota = int(input("CUANTAS NOTAS VAS A INGREAS"))
    total_nota = []
    for i in range(1, agregar_nota + 1):
        nota = float(input(f"NOTA {i} = "))
        total_nota.append(nota)
    notas_estudiantes[estudi] = total_nota 
    print(notas_estudiantes)
    continuar()
    menu()
    

def ver_notas():
    print()
    estudi = nombre()
    if estudi in estudiantes:
        print(f"***LAS NOTAS DEL ESTUDIANTE {estudi} SON : ***")
        print(notas_estudiantes[estudi])
        print()
    else:
        print("ESTE ESTUDIANTE NO EXISTE")
    continuar()
    menu()

def editar_nota():
    print()
    estudi = nombre()
    print(F"**EL ESTUDIANTE TIENE LAS SIGUIENTES NOTAS**")
    print(notas_estudiantes[estudi])
    cutos_cambios = int(input("CUANTOS CAMBIOS VAS A REALIZAR"))
    for i in range(1, cutos_cambios + 1):
        print(f"**CAMBIO {i}**")
        cambio = int((input("**QUE POSCISION DE LA NOTA QUIERES EDITAR**")))
        nota = float(input("QUE NOTA QUIERES INSERTAR"))
        notas_estudiantes[estudi][cambio - 1] = nota
        print("**CAMBIO REALIZADO**")
        print(notas_estudiantes[estudi])
        continuar()
    menu()

inicio()