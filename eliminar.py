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
        
def eliminar_sucursal():
    datos = cargar_datos()
    id_sucursal = input("Ingrese el ID de la sucursal a eliminar: ")
    
    if id_sucursal in datos:
        confirmar = input("¿Está seguro de que desea eliminar esta sucursal? (si/no): ").strip().lower()
        if confirmar == 'si':
            del datos[id_sucursal]
            guardar_datos(datos)
            print("Sucursal eliminada exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("ID de sucursal no encontrado.")