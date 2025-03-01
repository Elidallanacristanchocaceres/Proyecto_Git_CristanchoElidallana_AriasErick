# 🛠️ Funcionalidades Principales
### 1. Registrar Sucursal 📝
Permite agregar una nueva sucursal con los siguientes datos:

- ID de la sucursal (único).

- Nombre.

- Dirección.

- Teléfono.

- Responsable (ID del gerente o responsable).

Los datos se guardan en un archivo JSON (sucursales.json).

### 2. Editar Sucursal ✏️
Permite modificar los datos de una sucursal existente.

Se solicita el ID de la sucursal y se actualizan los campos necesarios.

### 3. Eliminar Sucursal 🗑️
Permite eliminar una sucursal existente.

Se solicita el ID de la sucursal y se confirma la eliminación.

### 4. Listar Sucursales 📋
Muestra todas las sucursales registradas en el sistema.

Se listan los detalles de cada sucursal (ID, nombre, dirección, teléfono y responsable).

### 5. Filtrar Sucursales 🔍
Permite buscar sucursales por nombre.

(Opcional) También se puede filtrar por estado (aunque esta funcionalidad aún no está implementada).

### 6. Salir del Programa 🚪
Cierra la aplicación de manera segura.

### 🖥️ Cómo Usar el Programa
Clona el repositorio:

````bash
git clone https://github.com/tuusuario/gestion-sucursales.git
````
Ejecuta el programa:

- Asegúrate de tener Python instalado.

- Ejecuta el archivo principal main.py:

````bash
python main.py
````
- Interactúa con el menú:

- El programa mostrará un menú con las opciones disponibles.

- Selecciona la opción deseada ingresando el número correspondiente.

### Manejo de datos:

Los datos se guardan automáticamente en el archivo sucursales.json.

Puedes modificar, eliminar o listar las sucursales según tus necesidades.

### 📂 Estructura del Proyecto
- main.py: Archivo principal que ejecuta el menú de opciones.

- nom_sucursal.py: Contiene las funciones para registrar, listar y filtrar sucursales.

- editar.py: Contiene la función para editar sucursales.

- eliminar.py: Contiene la función para eliminar sucursales.

- sucursales.json: Archivo JSON donde se almacenan los datos de las sucursales.

### 🛠️ Requisitos
Python 3.x instalado.

No se requieren librerías adicionales.

### 🚀 Ejemplo de Uso
-  Registrar una sucursal:

Selecciona la opción 1 en el menú.

Ingresa los datos solicitados (ID, nombre, dirección, teléfono y responsable).

Listar sucursales:

Selecciona la opción 4 en el menú.

Verás todas las sucursales registradas.

Editar una sucursal:

Selecciona la opción 3 en el menú.

Ingresa el ID de la sucursal y modifica los datos necesarios.

Eliminar una sucursal:

Selecciona la opción 2 en el menú.

Ingresa el ID de la sucursal y confirma la eliminación.

Filtrar sucursales:

Selecciona la opción 5 en el menú.

Ingresa el nombre de la sucursal que deseas buscar.
____
### 📬 Contacto
- 📧 Correo electrónico: cristanchodayana062017@gmail.com

- 💼 LinkedIn: [Elidallana Cristancho Caceres](https://www.linkedin.com/in/elidallanacristancho/)

¡Gracias por ser parte de esta aventura! 🚀✨
