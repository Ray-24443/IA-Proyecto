from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

while True:

    print("\n" + "=" * 50)
    print("      SISTEMA PREDICTOR INTELIGENTE")
    print("=" * 50)

    print("\n1. Predicción de Salario")
    print("2. Predicción de Vivienda")
    print("3. Predicción de Consumo Eléctrico")
    print("4. Predicción Climática")
    print("5. Salir")

    opcion = input("\nSeleccione una opción: ")

    # ---------------------------------------------------
    # SALARIO
    # ---------------------------------------------------
    if opcion == "1":

        X = np.array([
            [1, 40],
            [2, 40],
            [3, 42],
            [4, 45],
            [5, 45],
            [6, 48],
            [7, 50],
            [8, 50],
            [9, 52],
            [10, 55]
        ])

        y = np.array([
            10000, 13000, 16000, 19000, 23000,
            27000, 32000, 37000, 42000, 48000
        ])

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        modelo = LinearRegression()
        modelo.fit(X_train, y_train)

        experiencia = float(
            input("Años de experiencia: ")
        )

        horas = float(
            input("Horas trabajadas por semana: ")
        )

        resultado = modelo.predict(
            [[experiencia, horas]]
        )

        print(
            f"\nSalario estimado: "
            f"${resultado[0]:,.2f} MXN"
        )

    # ---------------------------------------------------
    # VIVIENDA
    # ---------------------------------------------------
    elif opcion == "2":

        X = np.array([
            [50,1],
            [70,2],
            [90,2],
            [110,3],
            [130,3],
            [150,4],
            [170,4],
            [190,5],
            [210,5],
            [230,6]
        ])

        y = np.array([
            800000,
            1200000,
            1500000,
            1800000,
            2200000,
            2600000,
            3000000,
            3400000,
            3800000,
            4200000
        ])

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        modelo = LinearRegression()
        modelo.fit(X_train, y_train)

        metros = float(
            input("Metros cuadrados: ")
        )

        habitaciones = int(
            input("Número de habitaciones: ")
        )

        resultado = modelo.predict(
            [[metros, habitaciones]]
        )

        print(
            f"\nPrecio estimado: "
            f"${resultado[0]:,.2f} MXN"
        )

    # ---------------------------------------------------
    # CONSUMO ELÉCTRICO
    # ---------------------------------------------------
    elif opcion == "3":

        X = np.array([
            [1,5],
            [2,6],
            [3,7],
            [4,8],
            [5,10],
            [6,12],
            [7,14],
            [8,16],
            [9,18],
            [10,20]
        ])

        y = np.array([
            50,80,110,140,180,
            220,260,310,360,420
        ])

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        modelo = LinearRegression()
        modelo.fit(X_train, y_train)

        horas = float(
            input("Horas de uso diario: ")
        )

        electrodomesticos = int(
            input("Número de electrodomésticos: ")
        )

        resultado = modelo.predict(
            [[horas, electrodomesticos]]
        )

        print(
            f"\nConsumo estimado: "
            f"{resultado[0]:.2f} kWh"
        )

    # ---------------------------------------------------
    # CLIMA
    # ---------------------------------------------------
    elif opcion == "4":

        X = np.array([
            [20,40],
            [22,45],
            [24,50],
            [26,55],
            [28,60],
            [30,65],
            [32,70],
            [34,75],
            [36,80],
            [38,85]
        ])

        y = np.array([
            10,15,20,30,40,
            55,65,75,85,95
        ])

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        modelo = LinearRegression()
        modelo.fit(X_train, y_train)

        temperatura = float(
            input("Temperatura (°C): ")
        )

        humedad = float(
            input("Humedad (%): ")
        )

        resultado = modelo.predict(
            [[temperatura, humedad]]
        )

        print(
            f"\nProbabilidad de lluvia: "
            f"{resultado[0]:.2f}%"
        )

    elif opcion == "5":

        print("\nGracias por utilizar el sistema.")
        break

    else:

        print("\nOpción inválida.")

    input("\nPresione ENTER para volver al menú...")