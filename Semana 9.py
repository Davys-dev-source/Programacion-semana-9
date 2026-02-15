"""
SISTEMA DE GESTIÓN DE INVENTARIO
Desarrollado bajo Programación Orientada a Objetos (POO)
Todo el sistema está contenido en un solo archivo.
"""

# ==============================
# CLASE PRODUCTO
# ==============================

class Producto:
    """
    Representa un producto dentro del inventario.
    Aplica encapsulamiento utilizando atributos privados.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # ===== GETTERS =====
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # ===== SETTERS =====
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("Error: La cantidad no puede ser negativa.")

    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio
        else:
            print("Error: El precio no puede ser negativo.")

    def __str__(self):
        return (f"ID: {self.__id} | "
                f"Nombre: {self.__nombre} | "
                f"Cantidad: {self.__cantidad} | "
                f"Precio: ${self.__precio:.2f}")


# ==============================
# CLASE INVENTARIO
# ==============================

class Inventario:
    """
    Gestiona la lista de productos.
    """

    def __init__(self):
        self.productos = []

    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        # Validar ID único
        if self.buscar_por_id(id_producto):
            print("Error: Ya existe un producto con ese ID.")
            return

        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        producto = self.buscar_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        producto = self.buscar_por_id(id_producto)
        if producto:
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)

            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)

            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def buscar_por_id(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    def buscar_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n=== INVENTARIO ACTUAL ===")
            for producto in self.productos:
                print(producto)


# ==============================
# MENÚ PRINCIPAL
# ==============================

def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                inventario.añadir_producto(id_producto, nombre, cantidad, precio)

            except ValueError:
                print("Error: Debe ingresar valores numéricos válidos.")

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            try:
                cantidad = input("Nueva cantidad (dejar vacío si no desea cambiar): ")
                precio = input("Nuevo precio (dejar vacío si no desea cambiar): ")

                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

            except ValueError:
                print("Error: Valores inválidos.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                print("\nResultados encontrados:")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# Punto de inicio del programa
if __name__ == "__main__":
    main()
