from clase import Clase
encendido= True
print("__________________________Crea tu propia clase__________________________")
nombreClase = str(input("Escribe el nombre de tu clase: "))
miClase= Clase(nombreClase)
print(f"Agrega un profesor para la clase {miClase.nombreClase}")
profesorNombre=str(input("Escriba el nombre del profesor: "))
profesorCelular=int(input("Ingrese el telefono del profesor: "))
profesorProfesion= str(input("Ingrese la profesion del profesor: "))
miClase.asignarProfesor(profesorNombre,profesorCelular,profesorProfesion)

while encendido:
    print(f"--------------------Bienvenido a la clase {miClase.nombreClase}--------------------")
    
    print("1.Ingresar estudiante \n2.Ingresar Nota a estudiante \n3.Informacion clase\n4.Mostrar estudiantes\n5.Eliminar estudiante\n6.Actualizar profesor\n7.Salir")
    opc= int(input("Ingrese la opcion: "))
    match opc:
        case 1:
            print("-------------------Ingresar estudiante-------------------")
            estudainteNombre=str(input("Escriba el nombre del estudiante: "))
            estudianteID=int(input("Ingrese el ID del estudiante: "))
            estudianteEdad= int(input("Ingrese la edad del estudiante: "))
            
            miClase.agregarEstudiante(estudainteNombre,estudianteID,estudianteEdad)
            miClase.mostrarEstudiantes()
            print("")
        case 2:
            print("-------------------Ingresar Nota a estudiante-------------------")
            estudainteNombre=str(input("Escriba el nombre del estudiante: "))
            estudianteNota=int(input("Escriba la nota del estudiante: "))
            miClase.agregarNotaEstudiante(estudainteNombre,estudianteNota)
            print("")
        case 3:
            print("-------------------Informacion clase-------------------")
            miClase.informacionClase()
        case 4:
            print("4.Mostrar estudiantes")
            miClase.mostrarEstudiantes()
        case 5: 
            print("-------------------Eliminar estudiante-------------------")
            estudainteNombre=str(input("Escriba el nombre del estudiante a eliminar: "))
            miClase.eliminarEstudiante(estudainteNombre)
            miClase.mostrarEstudiantes()
        case 6:
            print("-------------------Actualizar profesor-------------------")

            profesorNombre=str(input("Escriba el nombre del nuevo profesor: "))
            profesorCelular=int(input("Ingrese el telefono del nuevo profesor: "))
            profesorProfesion= str(input("Ingrese la profesion del nuevo profesor: "))
            miClase.asignarProfesor(profesorNombre,profesorCelular,profesorProfesion)

        case 7:
            print("-------------------Saliendo-------------------")
            break
        case _:
            print("opcion no valida")
