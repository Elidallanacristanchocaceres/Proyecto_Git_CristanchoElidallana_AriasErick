from nom_sucursal import registrar_sucursal
from eliminar_sucursal import eliminar_sucursal
from editar_sucursal import editar_sucursal

def main():
    eliminar_sucursal()
def main():
    editar_sucursal
def main():
    while True:
        print("\nGestion de sucursales")
        print("1. Registrar sucursal")
        print("2. Eliminar sucursal")
        print("3. Editar sucursal")

        opcion = input("Elige una de las opciones: ")

        if opcion == '1':
            registrar_sucursal()
        elif opcion == '2':
            eliminar_sucursal()
        elif opcion == '3':
            editar_sucursal
        elif opcion == '4':
            print("Salir de las opciones...")
            break
        else:
            print("La opcion que ingreso no es valida.")

if __name__ == "__main__":
    main()
