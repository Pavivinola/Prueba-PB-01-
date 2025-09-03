from dispositivo import Dispositivo
from computador import Computador
from tablet import Tablet
from telefono import Telefono
from tienda import Tienda

# Se crea una instancia de la clase Tienda
venta = Tienda()

# Se crean instancias de diferentes tipos de vehículos
mi_computador = Computador("HP", "Focus", 2500000, 32)             
mi_tablet = Tablet("Dynamo", "7050v", 750000, 12)  
mi_celular = Telefono("Panda", "P4v", 310000, 1200)          

# Usar el setter para modificar el precio de uno de ellos.
mi_tablet.set_precio(730000)

# o	Agregar los dispositivos a la tienda.
venta.agregar_dispositivo(mi_tablet)
venta.agregar_dispositivo(mi_computador)
venta.agregar_dispositivo(mi_celular)

# # Se muestra el resumen de la venta
venta.mostrar_catalogo()




# 4.	En el programa principal (main):
# o	Crear una tienda.
# o	Instanciar al menos una computadora, un teléfono y una tablet.


# o	Mostrar el catálogo completo.