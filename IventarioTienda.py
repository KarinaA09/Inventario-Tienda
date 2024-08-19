class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio
class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Comprobar si el ID ya existe
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID ya existe.")
            return
        self.productos.append(producto)

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.get_id() != id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                return
        print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return encontrados

    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        for p in self.productos:
            print(p)


def menu():
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    return input("Selecciona una opción: ")


def main():
    inventario = Inventario()

    while True:
        opcion = menu()

        if opcion == '1':
            id = input("Introduce el ID del producto: ")
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad: "))
            precio = float(input("Introduce el precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            print("Producto añadido exitosamente.")

        elif opcion == '2':
            id = input("Introduce el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
            print("Producto eliminado exitosamente.")

        elif opcion == '3':
            id = input("Introduce el ID del producto a actualizar: ")
            cantidad = input("Introduce la nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Introduce el nuevo precio (deja en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
            print("Producto actualizado exitosamente.")

        elif opcion == '4':
            nombre = input("Introduce el nombre del producto a buscar: ")
            productos = inventario.buscar_producto_por_nombre(nombre)
            if productos:
                print("Productos encontrados:")
                for p in productos:
                    print(p)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            print("Lista de productos en inventario:")
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")


if __name__ == "__main__":
    main()