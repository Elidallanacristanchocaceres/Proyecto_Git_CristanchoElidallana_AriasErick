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
        
def editar_sucursal():
    datos = cargar_datos()
    id_sucursal = input("Ingrese el ID de la sucursal a editar: ")
    
    if id_sucursal in datos:
        print("Datos actuales de la sucursal:")
        print(datos[id_sucursal])
        
        datos[id_sucursal] = {
            "nombre": input("Nuevo nombre de la sucursal: "),
            "direccion": input("Nueva dirección: "),
            "telefono": input("Nuevo número de teléfono: "),
            "responsable": input("Nuevo ID del gerente o responsable: ")
        }
        guardar_datos(datos)
        print("Sucursal actualizada exitosamente.")
    else:
        print("ID de sucursal no encontrado.")

    