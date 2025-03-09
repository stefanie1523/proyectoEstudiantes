from estudiante import Estudiante
from profesor import Profesor

class Clase:
    def __init__(self,nombreClase):
        self.estudiantes=[]
        self.nombreClase=nombreClase
        self.profesor=None

    def informacionClase(self):
        print(f"La clase es: {self.nombreClase}")
        self.profesor.mostrarInformacion()
        self.mostrarEstudiantes()

    def buscarEstudiantes(self,nombre):
        if not self.estudiantes:  # Si la lista está vacía
            print("No hay estudiantes en el grupo.")
            return None
          
        for i in range(len(self.estudiantes)):
            if nombre == self.estudiantes[i].nombre:
                return i
        print(f"No se encontró ningún estudiante con el nombre '{nombre}'.")
        return None

            
    def mostrarEstudiantes(self):
        if self.estudiantes:
            for i in range(len(self.estudiantes)):
                self.estudiantes[i].mostrarInformacion()
        else:
            print("No hay estudiantes")

    def agregarEstudiante(self,nombre,id,edad):
        estudiante= Estudiante(nombre,id,edad)
        self.estudiantes.append(estudiante)
    
    def eliminarEstudiante(self,nombre):
        estudianteEliminar= self.buscarEstudiantes(nombre)
        if estudianteEliminar !=None :
            del self.estudiantes[estudianteEliminar]
            print("Estudiante eliminado correctamente")
            #self.estudiantes.remove(self.estudiantes[estudianteEliminar])
        else:
            print(f"No se ha eliminado el estudiante")

    def agregarNotaEstudiante(self,nombre,nota):
        estudianteAgregar = self.buscarEstudiantes(nombre)

        if estudianteAgregar !=None:
            self.estudiantes[estudianteAgregar].agregarNota(nota)
            print("Se ha agregado la nota")
        else:
            print("No se ha agregado la nota ")

    def asignarProfesor(self,nombre,celular,profesion):
        self.profesor= Profesor(nombre,celular,profesion)
        self.profesor.mostrarInformacion()