class Estudiante:
    def __init__(self,nombre,id,edad,notas):
        self.nombre=nombre
        self.id=id
        self.edad=edad
        self.notas=[]
    
    def mostrarInformacion(self):
        return (f"El nombre del estudiante es: {self.nombre} y el id {self.id}")
    
    def mostrarNotas(self):
        return (f"Las notas del estudiante {self.nombre} son {self.notas}")
    
    def agregarNota(self,nota):
        self.notas.append(nota)

    def actualizarEdad(self,nuevaEdad):
        self.edad=nuevaEdad
    
    def promedioNotas(self):
        promedio=0
        for i in self.notas:
            promedio+=self.notas[i]
        return (f"El promedio de notas de {self.nombre} es de {self.mostrarNotas}")