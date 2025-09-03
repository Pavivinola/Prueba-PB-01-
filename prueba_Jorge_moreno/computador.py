from dispositivo import Dispositivo
# Computadora con atributo adicional ram (en GB).
class Computador(Dispositivo):
    def __init__(self, marca, modelo, precio, RAM):
        super().__init__(marca, modelo, precio)
        self.RAM = RAM
 # Cada clase debe sobrescribir el método descripcion() para mostrar sus propios datos.   
    def descripcion(self):
        return f" El computador marca: {self.marca}, del modelo: {self.modelo}, tiene de memoria RAM: {self.RAM} GB"
    

        
