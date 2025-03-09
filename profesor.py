class Profesor:
    def __init__(self,nombre,celular,profesion):
        self.nombre=nombre
        self.profesion=profesion
        self.celular=celular
    
    def mostrarInformacion(self):

        if self.nombre:
            print (f"El nombre del profesor es: {self.nombre} y la profesion es {self.profesion}")
        else:
            print (f"No hay profesor")
        
    
    def contactar(self):
        print (f"El nombre del profesor es: {self.nombre} y su numero es {self.celular}")
    
    def mostrarProfesion(self):
        return self.profesion
    