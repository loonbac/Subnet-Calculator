# 🌐 Generador de Subredes en Python con Tkinter 🎉

¡Bienvenido al **Generador de Subredes**! 🚀 Este es un proyecto divertido de una aplicación de escritorio desarrollada con Python usando la biblioteca Tkinter. Permite a los usuarios ingresar una dirección IP y una máscara de subred, para luego generar subredes basadas en la máscara ingresada y mostrar información útil sobre cada una de ellas.

## 🧑‍💻 Descripción general

La aplicación permite realizar las siguientes tareas:

1. **📶 Ingresar una dirección IP**: El usuario puede ingresar una dirección IP en formato estándar (por ejemplo, `192.168.1.1`).
2. **🔢 Ingresar una máscara en formato CIDR**: El usuario debe ingresar un número entre 0 y 31 que representa la cantidad de bits de la máscara (por ejemplo, `24` para una máscara `255.255.255.0`).
3. **🔍 Generar subredes**: Al ingresar la dirección IP y la máscara, la aplicación calcula las posibles subredes y las presenta en un menú desplegable, permitiendo al usuario seleccionar una máscara de subred específica para ver los detalles de las subredes correspondientes.
4. **💡 Mostrar detalles de las subredes**: Una vez seleccionada una máscara, la aplicación muestra información sobre las subredes generadas, como la dirección de red, la primera IP usable, la última IP usable y la dirección de broadcast de cada subred.

## 📝 Requisitos

Para ejecutar este proyecto, necesitas tener **Python 3.x** instalado en tu sistema. Además, se utiliza la biblioteca `tkinter` para la interfaz gráfica y `ipaddress` para la manipulación de redes IP. **`tkinter`** ya está incluida en las distribuciones estándar de Python, ¡así que no te preocupes por instalarla por separado! 😎

## 💾 Instalación

Sigue estos sencillos pasos para empezar:

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/generador-de-subredes.git
```

2. Navega al directorio del proyecto:

```bash
cd generador-de-subredes
```

3. Ejecuta el archivo Python para lanzar la aplicación:

## 🔧 Funcionalidad detallada

### 🌟 Interfaz de usuario

- **📥 Ingreso de IP**: Ingresa una dirección IP válida como `192.168.1.1`.
- **🔑 Ingreso de máscara CIDR**: Escribe un número de máscara de subred entre `0` y `31`, por ejemplo, `24` para `255.255.255.0`.
- **🚀 Botón "Generar Subredes"**: Al presionar este botón, la aplicación calculará todas las posibles subredes según la máscara CIDR que hayas proporcionado y las mostrará en un menú desplegable.
- **🎯 Selección de máscara para subredes**: Elige una máscara CIDR más específica para generar subredes.
- **👁️ Mostrar subredes**: Al seleccionar una máscara, haz clic en el botón "Mostrar Subredes" para ver la información detallada de las subredes generadas, como la dirección de red, la primera y última IP usable, y la dirección de broadcast.

### 🧠 Lógica del programa

1. **🔎 Obtención de datos**: Se obtiene la dirección IP y la máscara ingresada por el usuario.
2. **🛠️ Generación de subredes**: Según la máscara proporcionada, el programa calcula las subredes posibles con una máscara más específica.
3. **⚠️ Manejo de excepciones**: Si los valores ingresados son incorrectos, el programa muestra un mensaje de error. ¡Queremos evitar que te frustres! 😅

## 💡 Licencia

Este proyecto está licenciado bajo la **Licencia MIT** - consulta el archivo [LICENSE](LICENSE) para más detalles.
