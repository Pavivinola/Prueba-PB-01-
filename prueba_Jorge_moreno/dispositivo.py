class Dispositivo:
#atributos de la clase
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.__precio = precio
    
    #obtener el precio
    def get_precio(self):
        return self.__precio
        
    # Método setter para modificar el precio del vehículo
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:            # Se verifica que el nuevo precio sea mayor que 0
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor que 0")  # Se muestra mensaje de error si el precio no es válido

    # Método que retorna una descripción del vehículo
    def descripcion(self):
        return f"Vehículo marca: {self.marca}, modelo: {self.modelo}"  # Devuelve una cade
        
        
        
        
        
        





        