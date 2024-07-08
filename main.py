def menu():
    print("--------Sistema de Inventarios--------")
    print("1. Ingresar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("4. Lista de productos")
    print("5. Salir")

def seleccionar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            return opcion
        except ValueError:
            print("Opción no válida. Intente de nuevo.")

DB_FILE = "productos.txt"

def cargar_productos():
    nombres = []
    cantidades = []
    precios = []
    try:
        with open(DB_FILE, 'r') as file:
            for linea in file:
                nombre, cantidad, precio = linea.strip().split(',')
                nombres.append(nombre)
                cantidades.append(int(cantidad))
                precios.append(float(precio))
    except FileNotFoundError:
        pass 
    return nombres, cantidades, precios

def guardar_productos(nombres, cantidades, precios):
    with open(DB_FILE, 'w') as file:
        for nombre, cantidad, precio in zip(nombres, cantidades, precios):
            file.write(f"{nombre},{cantidad},{precio}\n")

def main():
    nombres, cantidades, precios = cargar_productos()
    cantidad_productos = len(nombres)

    while True:
        menu()
        opcion = seleccionar_opcion()

        if opcion == 1:
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            nombres.append(nombre)
            cantidades.append(cantidad)
            precios.append(precio)
            cantidad_productos += 1
            guardar_productos(nombres, cantidades, precios)
            print("Producto agregado exitosamente.")
        elif opcion == 2:
            nombre = input("Ingrese el nombre del producto a editar: ")
            if nombre in nombres:
                i = nombres.index(nombre)
                cantidades[i] = int(input("Ingrese la nueva cantidad: "))
                precios[i] = float(input("Ingrese el nuevo precio: "))
                guardar_productos(nombres, cantidades, precios)
                print("Producto editado exitosamente.")
            else:
                print("Producto no encontrado.")
        elif opcion == 3:
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            if nombre in nombres:
                i = nombres.index(nombre)
                del nombres[i]
                del cantidades[i]
                del precios[i]
                cantidad_productos -= 1
                guardar_productos(nombres, cantidades, precios)
                print("Producto eliminado exitosamente.")
            else:
                print("Producto no encontrado.")
        elif opcion == 4:
            print("\nLista de productos en inventario:\n")
            print("Nombre\t\tCantidad\t\tPrecio")
            for i in range(cantidad_productos):
                print(f"{nombres[i]}\t\t{cantidades[i]}\t\t{precios[i]:.2f}")
        elif opcion == 5:
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
