from nom_sucursal import registrar_sucursal
from nom_sucursal import eliminar_sucursal
from nom_sucursal import editar_sucursal
from nom_sucursal import listar_sucursales
from nom_sucursal import filtrar_sucursales

def main():
    while True:
        print("\nGestión de sucursales")
        print("1. Registrar sucursal")
        print("4. Listar sucursales")
        print("5. Filtrar sucursales")
        print("6. Salir")

        opcion = input("Elige una de las opciones: ").strip()

        if opcion == '1':
            registrar_sucursal()
        elif opcion == '4':
            listar_sucursales()
        elif opcion == '5':
            filtrar_sucursales()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("La opción que ingresó no es válida. Por favor, elija una opción entre 1 y 6.")

if __name__ == "__main__":
    main()