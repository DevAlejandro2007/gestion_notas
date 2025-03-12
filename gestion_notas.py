estudiantes = []
notas_estudiantes = {}

def inicio(): 
    print("""
    --------------------
    ---SOFTWARE NOTAS---
    --------------------
          """)
    input("OPRIME ENTER PARA EMPEZAR")
    menu()

def menu():
    print("""
    ---------------
    -----MENU------
    ---------------
    """)

    menu = int(input("""
    1. INSERTAR NOTAS
    2. VER NOTAS DE ESTUDIANTE
    3. EDITAR NOTAS DE ESTUDIANTE
    4. SALIR 
                 
    ESCRIBE LA OPCION QUE DECEE EJECUTAR
    """))
    if menu == 1:
        notas()


def notas():
    print()
    profe = input("NOMBRE DEL PROFESOR QUE INSERTARA NOTAS \n")
    print()
    estudi = input("NOMBRE DEL ESTUDIANTE AL QUE SE INSERTARA NOTAS \n")
    estudiantes.append(estudi)
    agregar_nota = int(input("CUANTAS NOTAS VAS A INGREAS"))
    total_nota = []
    for i in range(1, agregar_nota + 1):
        nota = float(input(f"NOTA {i} = "))
        total_nota.append(nota)
        notas_estudiantes[estudi] = profe
    notas_estudiantes[estudi] = total_nota 
    
    
    print(notas_estudiantes)
    menu()
    print()

        
        


        
        


  
    







inicio()