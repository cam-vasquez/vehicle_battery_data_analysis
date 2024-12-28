# Importar las librerías necesarias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import numpy as np

# Configurar página
st.set_page_config(page_title="Visualización y Modelado", layout="wide")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv("data/ev_charging_patterns.csv")  # Cambia la ruta si es necesario

df = load_data()

# Título de la aplicación
st.title("Visualización y Modelado de Datos")
st.subheader("Vista previa del conjunto de datos cargado desde el archivo local:")

# Mostrar datos
st.dataframe(df.head())

# Manejo de valores nulos
st.subheader("Limpieza de datos: Reemplazo de valores nulos")
for column in df.select_dtypes(include='number').columns:
    if df[column].isnull().sum() > 0:
        median_value = df[column].median()
        df[column].fillna(median_value, inplace=True)
        st.write(f"Valores nulos en '{column}' reemplazados con la mediana ({median_value})")

st.subheader("Estadísticas descriptivas después de la limpieza")
st.write(df.describe())

# Variables categóricas y numéricas
categorical_features = ['Vehicle Model', 'Charging Station Location', 'Charger Type', 'User Type']
numeric_features = ['Battery Capacity (kWh)', 'Energy Consumed (kWh)', 'Charging Duration (hours)']

# ---------------- Preprocesamiento ----------------
numeric_transformer = Pipeline(steps=[('scaler', StandardScaler())])
categorical_transformer = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

X = preprocessor.fit_transform(df)

# ---------------- Reducción de Dimensiones (PCA) ----------------
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualización PCA
st.subheader("Visualización PCA")
fig, ax = plt.subplots(figsize=(6, 4)) 
scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.7, cmap='viridis', edgecolor='k')
ax.set_title("Reducción de Dimensiones con PCA")
ax.set_xlabel("Componente Principal 1")
ax.set_ylabel("Componente Principal 2")
legend = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend)
st.pyplot(fig)

# ---------------- K-Means y Clustering ----------------
st.subheader("Método del Codo para determinar el número óptimo de Clusters")
range_clusters = range(2, 8)
inertia = []

for k in range_clusters:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

fig, ax = plt.subplots(figsize=(6, 4))  # Tamaño reducido
ax.plot(range_clusters, inertia, marker='o')
ax.set_title("Método del Codo")
ax.set_xlabel("Número de Clusters")
ax.set_ylabel("Inercia")
st.pyplot(fig)

# Aplicar K-Means con k=4
kmeans_pca = KMeans(n_clusters=4, random_state=42)
clusters_pca = kmeans_pca.fit_predict(X_pca)

# Visualización de clusters
st.subheader("Visualización de Clusters con PCA")
fig, ax = plt.subplots(figsize=(6, 4))  
scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters_pca, cmap='viridis', alpha=0.7, edgecolor='k')
ax.set_title(f"Clusters con PCA (k=4)")
ax.set_xlabel("Componente Principal 1")
ax.set_ylabel("Componente Principal 2")
fig.colorbar(scatter, label='Cluster')
st.pyplot(fig)

# ---------------- Visualización 3D ----------------
st.subheader("Gráfico 3D de las Características Originales")
x_col = st.selectbox("Selecciona la columna para el eje X", numeric_features)
y_col = st.selectbox("Selecciona la columna para el eje Y", numeric_features)
z_col = st.selectbox("Selecciona la columna para el eje Z", numeric_features)

fig = plt.figure(figsize=(8, 6))  
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df[x_col], df[y_col], df[z_col], c=clusters_pca, cmap='viridis', marker='o')
ax.set_xlabel(x_col)
ax.set_ylabel(y_col)
ax.set_zlabel(z_col)
ax.set_title("Gráfico 3D con Clustering")
st.pyplot(fig)


# Agregar imports necesarios
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_squared_error, r2_score

# Nueva sección: Árbol de Decisión
st.header("Modelo de Árbol de Decisión")

# Selección de características y variable objetivo
st.subheader("Selecciona las características y la variable objetivo para el modelo")
features = st.multiselect("Selecciona las características predictoras", numeric_features)
target = st.selectbox("Selecciona la variable objetivo", numeric_features)

# Verificar si hay selección válida
if features and target:
    X = df[features]
    y = df[target]

    # Dividir en conjunto de entrenamiento y prueba
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=4254)

    # Entrenar el modelo
    tree_model = DecisionTreeRegressor(random_state=42)
    tree_model.fit(X_train, y_train)

    # Realizar predicciones
    y_pred = tree_model.predict(X_test)

    # Mostrar métricas del modelo
    st.subheader("Métricas del modelo")
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    st.write(f"**Mean Squared Error (MSE):** {mse}")
    st.write(f"**R² Score:** {r2}")

    # Visualizar el árbol de decisión
    st.subheader("Visualización del Árbol de Decisión")
    fig, ax = plt.subplots(figsize=(20, 10))
    plot_tree(tree_model, feature_names=features, filled=True, rounded=True, ax=ax)
    st.pyplot(fig)

else:
    st.warning("Por favor, selecciona las características y la variable objetivo para entrenar el modelo.")

# Agregar imports necesarios
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_squared_error, r2_score

# Nueva sección: Árbol de Decisión
st.header("Modelo de Árbol de Decisión")

# Selección de características y variable objetivo
st.subheader("Selecciona las características y la variable objetivo para el modelo")
features = st.multiselect("Selecciona las características predictoras", numeric_features)
target = st.selectbox("Selecciona la variable objetivo", numeric_features)

# Verificar si hay selección válida
if features and target:
    X = df[features]
    y = df[target]

    # Dividir en conjunto de entrenamiento y prueba
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=4254)

    # Entrenar el modelo
    tree_model = DecisionTreeRegressor(random_state=42)
    tree_model.fit(X_train, y_train)

    # Realizar predicciones
    y_pred = tree_model.predict(X_test)

    # Mostrar métricas del modelo
    st.subheader("Métricas del modelo")
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    st.write(f"**Mean Squared Error (MSE):** {mse}")
    st.write(f"**R² Score:** {r2}")

    # Visualizar el árbol de decisión
    st.subheader("Visualización del Árbol de Decisión")
    fig, ax = plt.subplots(figsize=(20, 10))
    plot_tree(tree_model, feature_names=features, filled=True, rounded=True, ax=ax)
    st.pyplot(fig)

else:
    st.warning("Por favor, selecciona las características y la variable objetivo para entrenar el modelo.")
