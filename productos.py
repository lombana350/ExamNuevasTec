
class RegistroProducto:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, id, nombre, descripcion, costo, cantidad, MargenDeVenta):
        PrecioVenta = round(costo / (1 - MargenDeVenta),2)
        producto = {
            'id': id,
            'nombre': nombre,
            'descripcion': descripcion,
            'costo': costo,
            'cantidad': cantidad,
            'PrecioVenta': PrecioVenta
        }
        self.productos[id] = producto

    def imprimir_productos(self):
        print("Listado de productos:")
        for id, producto in self.productos.items():
            print(f"ID: {id}, Nombre: {producto['nombre']}, Descripción: {producto['descripcion']}, "
                  f"Costo: {producto['costo']}, Cantidad: {producto['cantidad']}, Precio de Venta: {producto['PrecioVenta']}")


registro = RegistroProducto()
registro.registrar_producto(1, 'Mango', 'Fruta', 10.0, 50, 0.2)
registro.registrar_producto(2, 'Cebolla', 'Vegetal', 15.0, 30, 0.15)
registro.imprimir_productos()
