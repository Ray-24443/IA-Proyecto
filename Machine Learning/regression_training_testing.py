# Importa la función train_test_split de Scikit-Learn.
# Esta función permite dividir automáticamente un conjunto
# de datos en datos de entrenamiento y datos de prueba.
from sklearn.model_selection import train_test_split

# Features (X)
# Representan la información de entrada del modelo.
# En este ejemplo son las horas de estudio.
X = [[2], [4], [6], [8], [10]]

# Labels (y)
# Son los valores que queremos que el modelo aprenda a predecir.
# En este ejemplo son las calificaciones obtenidas.
y = [60, 75, 85, 95, 100]

# Divide los datos en dos grupos:
# - Datos de entrenamiento (80%)
# - Datos de prueba (20%)
#
# X_train -> Features para entrenamiento
# X_test  -> Features para prueba
# y_train -> Labels para entrenamiento
# y_test  -> Labels para prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2
)

# Muestra los datos utilizados para entrenar el modelo
print("Datos de entrenamiento:")
print(X_train)

# Muestra los datos utilizados para evaluar el modelo
print("Datos de prueba:")
print(X_test)