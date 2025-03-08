from estudiante import Estudiante
from profesor import Profesor

class Clase:
    def __init__(self,nombreClase):
        self.estudiantes=None
        self.nombreClase=nombreClase
        self.profesor=None
    def informacionClase(self):
        self.profesor
    def buscarEstudiantes(self,nombre):
        if self.estudiantes:

            print("No hay estudiantes añadidos")
            return None
        else:
            for i in self.estudiantes:
                if nombre== self.estudiantes[i]:
                    print(f"El estudiante buscado es {self.estudiantes[i]}")
                    return i
            
            print(f"No se encontro a el estudiante{nombre}")
            return None
    def mostrarEstudiantes(self):
        if self.estudiantes:
            for i in self.estudiantes:
                print (self.estudiantes[i].mostrarInformacion)

    def agregarEstudiante(self,nombre,id,edad,):
        estudiante= Estudiante(nombre,id,edad)
        self.estudiantes.append(estudiante)
    def eliminarEstudiante(self,nombre):
        estudianteEliminar= self.buscarEstudiantes(nombre)
        if estudianteEliminar:
            print(f"Se va a eliminar el estudiante {self.estudiantes[estudianteEliminar]}")
            self.estudiantes.remove(estudianteEliminar)
        else:
            print(f"No se ha eliminado el estudiante")

    def agregarNotaEstudiante(self,nombre,nota):
        estudianteAgregar= self.buscarEstudiantes(nombre)
        if estudianteAgregar:
            self.estudiantes[estudianteAgregar].agregarNota(nota)
            print("Se ha agregado la nota")
        else:
            print("No se ha agregado la nota ")

    def asignarProfesor(self,nombre,celular,profesion):
        self.profesor= Profesor(nombre,celular,profesion)
        self.profesor.mostrarInformacion