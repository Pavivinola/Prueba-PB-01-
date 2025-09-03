from dispositivo import Dispositivo
# Tablet con atributo adicional pulgadas (tamaño de pantalla).
class Tablet(Dispositivo):
    def __init__(self, marca, modelo, precio, pulgadas):
        super().__init__(marca, modelo, precio)
        self.pulgadas = pulgadas
    def descripcion(self):
        return f" El tablet marca: {self.marca}, del modelo: {self.modelo}, tiene pantalla de : {self.pulgadas} mega pixeles"