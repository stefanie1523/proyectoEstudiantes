class Estudiante:
    def __init__(self,nombre,id,edad):
        self.nombre=nombre
        self.id=id
        self.edad=edad
        self.notas=[]
    
    def mostrarInformacion(self):
        print (f"El nombre del estudiante es: {self.nombre} y el id {self.id}")
    
    def mostrarNotas(self):
        return (f"Las notas del estudiante {self.nombre} son {self.notas}")
    
    def agregarNota(self,nota):
        self.notas.append(nota)

    def actualizarEdad(self,nuevaEdad):
        self.edad=nuevaEdad
    
    def promedioNotas(self):
    
        if not self.notas:
            return "No hay notas"
        else:
            promedio=0
            for i in range(len(self.notas)):
                promedio+=self.notas[i]
            return (f"El promedio de notas de {self.nombre} es de {self.mostrarNotas}")