# src/grafica.py

import pandas as pd

def leer_datos(archivo):
    return pd.read_csv(archivo)

def calcular_rendimiento(data):
    data['rendimiento'] = data['kilometros'] / data['combustible']
    return data

def guardar_datos(data, archivo_salida):
    data.to_csv(archivo_salida, index=False)

def main():
    datos = leer_datos('data/datos_combustible.csv')
    datos_rendimiento = calcular_rendimiento(datos)
    guardar_datos(datos_rendimiento, 'data/datos_rendimiento.csv')
    print("Datos de rendimiento calculados y guardados en 'data/datos_rendimiento.csv'")

if __name__ == "__main__":
    main()
