from clase import Clase
encendido= True
print("__________________________Crea tu propia clase__________________________")
nombreClase = str(input("Escribe el nombre de tu clase: "))
miClase= Clase(nombreClase)
print(f"Agrega un profesor para la clase {miClase.nombreClase}")
profesorNombre=str(input("Escriba el nombre del profesor: "))
profesorCelilar=int(input("Ingrese el telefono del profesor: "))
profesorProfesion= str(input("Ingrese la profesion del profesor: "))

while encendido:
    print(f"--------------------Bienvenido a la clase {miClase.nombreClase}--------------------")
    print("1.Ingresar estudiante \n2.Ingresar Nota a estudiante \n3.Informacion clase\n4.Mostrar estudiantes\n5.Eliminar estudiante\n6.Actualizar profesor\n7.Informacion de la clase\n8.Salir")
    break