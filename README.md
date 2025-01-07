# Calculadora Web con Flask, HTML, CSS y JavaScript

¡Bienvenido a mi proyecto de calculadora web! Este proyecto utiliza **Flask** para el back-end, junto con **HTML**, **CSS** y **JavaScript** para crear una aplicación funcional que permite realizar operaciones matemáticas básicas. La calculadora tiene una interfaz interactiva que puedes utilizar directamente en tu navegador.

## 🚀 Características

- **Interfaz de usuario**: Diseñada con **HTML** y estilizada con **CSS** para una apariencia moderna y responsiva.
- **Funciones principales**:
  - ➕ Suma
  - ➖ Resta
  - ✖️ Multiplicación
  - ➗ División
- **Back-end en Flask (Python)**: Recibe las expresiones matemáticas desde el frontend, las evalúa y devuelve el resultado.
- **Lógica en JavaScript**: Maneja la interacción con los botones, mostrando las expresiones y resultados en tiempo real.

## ⚙️ Cómo funciona

1. La interfaz de la calculadora está construida utilizando **HTML** para la estructura y **CSS** para el estilo visual.
2. Los usuarios pueden interactuar con los botones para crear operaciones matemáticas (como "5 + 7").
3. Cuando se presiona el botón de igual (`=`), el JavaScript envía la expresión al **back-end** de Flask.
4. El **back-end en Python** evalúa la operación utilizando la función `eval()` y devuelve el resultado a la interfaz.
5. El resultado se muestra en tiempo real en la pantalla de la calculadora.

## 🛠️ Estructura del Proyecto

La estructura del proyecto es la siguiente:

calculator/ ├── app.py # Archivo principal del servidor Flask. ├── templates/ # Carpeta con las plantillas HTML. │ └── index.html # Plantilla HTML para la calculadora. ├── static/ # Carpeta con archivos estáticos como CSS y JavaScript. │ ├── css/ │ │ └── styles.css # Estilos CSS para la calculadora. │ └── js/ │ └── script.js # Lógica JavaScript para la interacción.

markdown
Copiar código

### **Archivos clave**

1. **`app.py`**:
   - El archivo `app.py` es el servidor de **Flask** que maneja las solicitudes de la calculadora, evalúa las expresiones matemáticas y devuelve los resultados al cliente.
   
2. **`index.html`**:
   - Este archivo HTML define la estructura de la calculadora, incluyendo los botones y el área para mostrar el resultado.

3. **`styles.css`**:
   - El archivo CSS define el diseño visual de la calculadora, con un estilo limpio y moderno.

4. **`script.js`**:
   - El archivo JavaScript gestiona la interacción de los usuarios con la calculadora, actualizando el campo de entrada y mostrando los resultados.

## 💻 Ejecución del Proyecto

1. **Instalar Flask**:
   Si no tienes Flask instalado, puedes hacerlo con:

   ```bash
   pip install flask
Iniciar el servidor: Para iniciar el servidor, ejecuta el archivo app.py:

bash
Copiar código
python app.py
Accede a la calculadora: Abre tu navegador y visita http://127.0.0.1:5000/ para usar la calculadora. 
