
# Módulos en Python

## Comenzando

Sigue estos pasos para iniciar y trabajar con este proyecto:

1. **Clona el repositorio:**
	```bash
	git clone <url-del-repositorio>
	cd modulos
	```

2. **Crea y activa el entorno virtual:**
	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```

3. **Instala las dependencias:**
	```bash
	pip install streamlit sympy
	```

4. **Ejecuta una app de ejemplo con Streamlit:**
	```bash
	streamlit run archivo_ejemplo.py
	```

Reemplaza `archivo_ejemplo.py` por el nombre del archivo que desees ejecutar.

Un módulo en Python es un archivo que contiene definiciones y declaraciones de Python, como funciones, variables y clases, que pueden ser reutilizadas en otros programas. Los módulos permiten organizar el código en partes más pequeñas y manejables, facilitando la reutilización y el mantenimiento.

## ¿Por qué usar módulos?

- **Reutilización de código:** Permiten escribir funciones y clases una sola vez y usarlas en diferentes programas.
- **Organización:** Ayudan a dividir programas grandes en archivos más pequeños y lógicos.
- **Mantenimiento:** Facilitan la actualización y corrección de errores en el código.

## Tipos de módulos

1. **Módulos estándar:** Vienen incluidos con Python, como `math`, `os`, `sys`, entre otros.
2. **Módulos de terceros:** Son desarrollados por la comunidad y se instalan con herramientas como `pip`.
3. **Módulos propios:** Son archivos `.py` creados por el propio programador.

## Cómo importar módulos

Para usar un módulo, se utiliza la instrucción `import`:

```python
import math
print(math.pi)
```

También se pueden importar funciones o variables específicas:

```python
from math import sqrt
print(sqrt(16))
```

Los módulos son una parte fundamental de la programación en Python y permiten crear aplicaciones más robustas y escalables.

---

## Streamlit

Streamlit es un módulo de Python diseñado para crear aplicaciones web interactivas de manera sencilla y rápida, especialmente orientadas a la visualización de datos y prototipos de ciencia de datos.

### Funcionalidades mínimas de Streamlit
- Crear interfaces web con pocas líneas de código.
- Mostrar texto, datos, gráficos y widgets interactivos (sliders, botones, selectores, etc.).
- Actualización automática de la interfaz al modificar el código.
- Integración con librerías de visualización como Matplotlib, Plotly y Altair.

#### Ejemplo básico:
```python
import streamlit as st
st.title('Hola, Streamlit!')
st.write('Esta es una app web sencilla.')
```

---

## Sympy

Sympy es un módulo de Python para matemáticas simbólicas, es decir, permite realizar cálculos algebraicos exactos, manipulación de expresiones y resolución de ecuaciones de manera simbólica.

### Funcionalidades mínimas de Sympy
- Definir símbolos y expresiones algebraicas.
- Simplificar y expandir expresiones matemáticas.
- Resolver ecuaciones algebraicas y diferenciales.
- Calcular derivadas, integrales y límites.
- Generar representaciones en LaTeX y visualización de expresiones.

#### Ejemplo básico:
```python
import sympy as sp
x = sp.symbols('x')
expresion = x**2 + 2*x + 1
resultado = sp.expand(expresion)
print(resultado)
```
