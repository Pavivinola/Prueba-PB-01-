# Importa la clase dispositivo desde el módulo dispositivo
from dispositivo import Dispositivo

# Definición de la clase Tienda
class Tienda:
    # Constructor que inicializa la lista de pedidos (vehículos agregados)
    def __init__(self):
        self.pedidos = []  # o	Una lista que almacene los dispositivos.


# 3.	Crear la clase Tienda con:


# o	Método mostrar_catalogo() → 

    # Método para agregar un dispositivo a la tienda
    def agregar_dispositivo(self, dispositivo):
        
        print(f"Agregado: {dispositivo.descripcion()} - Precio: ${dispositivo.get_precio()}")
        self.pedidos.append(dispositivo) 

    # o	Método agregar_dispositivo(dispositivo) → agrega un dispositivo a la lista.
    def mostrar_catalogo(self):
        print("--- Recumen de la Venta ---")  # Encabezado del resumen
        total = 0  # Variable para acumular el total a pagar
        for dispositivo in self.pedidos:
            # recorre la lista y muestra la descripción y el precio de cada dispositivo, además de calcular el valor total de inventario.
            print(f"{dispositivo.descripcion()} \n ${dispositivo.get_precio()}")
            total += dispositivo.get_precio()  # Suma el precio al total
        print(f"Total a pagar: ${total}")  # Muestra el total acumulado
