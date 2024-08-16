import json
from datetime import datetime


ARCHIVO_DATOS = "sucursales.json"

def cargar_datos():
    try:
        with open(ARCHIVO_DATOS, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def guardar_datos(datos):
    with open(ARCHIVO_DATOS, "w") as archivo:
        json.dump(datos, archivo, indent=4)

def registrar_sucursal():
    datos = cargar_datos()
    
    id_sucursal = input("Ingrese un ID para la sucursal: ")
    
    if id_sucursal in datos:
        print("ID ya existe. Use otro ID.")
        return
    
    sucursal = {
        "nombre": input("Nombre de la sucursal: "),
        "direccion": input("Dirección completa: "),
        "telefono": input("Número de teléfono: "),
        "responsable": input("ID del gerente o responsable: ")
    }
    
    datos[id_sucursal] = sucursal
    guardar_datos(datos)
    print("Sucursal registrada exitosamente.")



def listar_sucursales():
    datos = cargar_datos()
    if not datos:
        print("No hay sucursales registradas.")
        return

    print("\nLista de Sucursales:")
    for id_sucursal, sucursal in datos.items():
        print(f"ID: {id_sucursal}")
        print(f"Nombre: {sucursal['nombre']}")
        print(f"Dirección: {sucursal['direccion']}")
        print(f"Teléfono: {sucursal['telefono']}")
        print(f"Responsable: {sucursal['responsable']}")
        print()

def filtrar_sucursales():
    datos = cargar_datos()
    if not datos:
        print("No hay sucursales registradas.")
        return

    filtro = input("Filtrar por nombre o estado (nombre/estado): ").strip().lower()
    if filtro == 'nombre':
        nombre = input("Ingrese el nombre de la sucursal: ").strip().lower()
        print("\nSucursales encontradas:")
        for id_sucursal, sucursal in datos.items():
            if nombre in sucursal['nombre'].lower():
                print(f"ID: {id_sucursal}")
                print(f"Nombre: {sucursal['nombre']}")
                print(f"Dirección: {sucursal['direccion']}")
                print(f"Teléfono: {sucursal['telefono']}")
                print(f"Responsable: {sucursal['responsable']}")
                print()
    elif filtro == 'estado':
        # Este campo no está implementado en los datos actuales
        print("Filtrado por estado no implementado aún.")
    else:
        print("Filtro no válido.")

def main():
    while True:
        print("\nGestión de sucursales")
        print("1. Registrar sucursal")
        print("2. Eliminar sucursal")
        print("3. Editar sucursal")
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
            print("Esta opcion es incorrecta.")

if __name__ == "__main__":
    main()
