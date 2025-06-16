# tratamiento de datos
import pandas as pd
import numpy as np

# visualizaciones
import matplotlib.pyplot as plt
import seaborn as sns

def mostrar_distribuciones(df, columnas, objetivo='y'):

    '''funcion que permite visualizar la distribución de las columnas del DataFrame, condicionada por una variable objetivo ('y').
    podemos ver como se comportan distintas variables según el resultado de la variable objetivo'''
    for col in columnas:
        plt.figure(figsize=(10, 5))

        if pd.api.types.is_numeric_dtype(df[col]):
            sns.histplot(data=df, x=col, hue=objetivo, kde=True, bins=30, element="step")
            plt.title(f'Distribución de {col} por {objetivo}')
        
        else:
            orden = df[col].value_counts().index
            sns.countplot(data=df, x=col, hue=objetivo, order=orden)
            plt.title(f'Distribución de {col} por {objetivo}')
            plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

def graficas_tasas_conversion(df, var_predictora, var_predecir, type='line',order= None):
    x, y = var_predictora, var_predecir

    ''' funcion que permite visualizar la tasa de conversión de una variable objetivo en función de una 
    variable predictora categórica o numérica '''

    grupo = df.groupby(x)[y].mean().mul(100).rename('tasa_conversion').reset_index()

    if type == 'line':
        plt.figure(figsize=(10,5))
        sns.lineplot(x= var_predictora, y='tasa_conversion', data=grupo)
        plt.grid()
    elif type == 'bar':
        plt.figure(figsize=(14,5))
        sns.barplot(x= var_predictora, y='tasa_conversion', data=grupo, order=order)
        plt.grid()
    elif type == 'scatter':
        plt.figure(figsize=(10,5))
        sns.scatterplot(x= var_predictora, y='tasa_conversion', data=grupo)
        plt.grid()


def merge_graficas_tasas_conversion(df_merge, var_predictora, var_predecir, type='line',order= None):
    x, y = var_predictora, var_predecir

    grupo = df_merge.groupby(x)[y].mean().mul(100).rename('tasa_conversion').reset_index()

    if type == 'line':
        plt.figure(figsize=(15,5))
        sns.lineplot(x= var_predictora, y='tasa_conversion', data=grupo)
        plt.grid()
    elif type == 'bar':
        plt.figure(figsize=(14,5))
        sns.barplot(x= var_predictora, y='tasa_conversion', data=grupo, order=order)
        plt.grid()
    elif type == 'scatter':
        plt.figure(figsize=(10,5))
        sns.scatterplot(x= var_predictora, y='tasa_conversion', data=grupo)
        plt.grid()