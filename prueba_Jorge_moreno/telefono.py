from dispositivo import Dispositivo
# Telefono con atributo adicional camara (en megapíxeles).
class Telefono(Dispositivo):
    def __init__(self, marca, modelo, precio, camara):
      super().__init__(marca, modelo, precio)
      self.camara = camara
 # Cada clase debe sobrescribir el método descripcion() para mostrar sus propios datos.   
    def descripcion(self):
        return f" El telefono marca: {self.marca}, del modelo: {self.modelo} tiene una cámara de : {self.camara} mega pixeles"
    
    




# Cada clase debe sobrescribir el método descripcion() para mostrar sus propios datos.
