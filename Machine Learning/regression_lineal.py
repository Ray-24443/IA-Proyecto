# ================================
# 1. IMPORTAR LIBRERÍA NECESARIA
# ================================

# Importa train_test_split para dividir los datos en entrenamiento y prueba
from sklearn.model_selection import train_test_split

# Importa el modelo de regresión lineal
from sklearn.linear_model import LinearRegression


# ================================
# 2. CREAR LOS DATOS (DATASET)
# ================================

# Features (X)
# Son las variables de entrada: horas de estudio
X = [[2], [4], [6], [8], [10]]

# Labels (y)
# Son los resultados reales: calificaciones obtenidas
y = [60, 75, 85, 95, 100]


# ================================
# 3. DIVIDIR LOS DATOS
# ================================

# Se divide el conjunto de datos en:
# - entrenamiento (para aprender)
# - prueba (para evaluar)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,      # 20% para prueba
    random_state=42     # asegura mismos resultados siempre
)


# ================================
# 4. CREAR EL MODELO
# ================================

# Se crea el modelo de regresión lineal
model = LinearRegression()


# ================================
# 5. ENTRENAR EL MODELO
# ================================

# El modelo aprende la relación entre X_train y y_train
model.fit(X_train, y_train)


# ================================
# 6. HACER PREDICCIONES
# ================================

# El modelo intenta predecir resultados usando datos de prueba
predictions = model.predict(X_test)


# ================================
# 7. EVALUAR EL MODELO
# ================================

# Calcula qué tan bien funciona el modelo
score = model.score(X_test, y_test)

print("================================")
print("RESULTADOS DEL MODELO")
print("================================")

print("Datos de prueba (X_test):")
print(X_test)

print("\nPredicciones del modelo:")
print(predictions)

print("\nValores reales (y_test):")
print(y_test)

print("\nPrecisión del modelo (R^2 score):")
print(score)