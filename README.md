# Aplicación Streamlit

Esta es una aplicación web desarrollada con Streamlit para realizar análisis interactivos y visualizaciones dinámicas. Siga los pasos a continuación para configurar y ejecutar el proyecto.

---
## 📂 Estructura del proyecto
```bash
vehicle_battery_data_analysis/
├── Inicio.py                     # Archivo principal de la aplicación
├── requirements.txt              # Dependencias del proyecto
├── pages/                        # Carpeta con pages
│   ├── 1_📊_EDA.py              # Módulo para análisis exploratorio de datos
│   ├── 2_📋_Hipotesis.py        # Módulo para carga de datos
│   └── 3_💻_Modelo.py           # Módulo para visualizaciones
├── modulos/                     # Carpeta con módulos adicionales
│   ├── eda.py                   # Módulo para análisis exploratorio de datos
│   └── hipotesis.py             # Módulo para hipotesis
├── utils/
│   ├── picture1.png             # Archivo estático 1
│   ├── picture2.png             # Archivo estático 2
│   └── picture3.png             # Archivo estático 3
└── venv/                        # Ambiente virtual (no incluido en el repositorio)
```
---
## 🚀 Pasos para ejecutar la aplicación

### 1. Crear el ambiente virtual
Cree un ambiente virtual para instalar las dependencias de manera aislada.
 ```bash
python -m venv venv

```
### 2. Activar el ambiente virtual
En Windows:
```bash
.\venv\Scripts\activate
```

### 3. Instalar dependencias
Instale las dependencias necesarias desde el archivo requirements.txt.
 ```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
Ejecute la aplicación Streamlit.
```bash
streamlit run Inicio.py
```

### 5. Salir del ambiente virtual (opcional)
```bash
deactivate
```
---
## ¡Gracias por usar esta aplicación! 🎉
