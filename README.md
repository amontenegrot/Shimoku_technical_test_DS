# Data Scientist - Prueba técnica
Estamos trabajando en un algoritmo de puntuación de clientes potenciales para un cliente que tiene una aplicación SaaS de gestión de eventos. Tu trabajo consiste en recibir los datos en bruto del cliente y prepararlos para entrenar un algoritmo de clasificación que prediga la probabilidad de conversión de cada oportunidad de venta.

Recibirá 2 conjuntos de datos que reflejan las fases del proceso de ventas del cliente: **leads.csv** y **offers.csv**. La columna objetivo será Status del conjunto de datos de offers, que indica si un cliente ha comprado el producto.

## Leads
Datos de todos los clientes potenciales.

## Offers
Clientes que llegaron al menos a la reunión de demostración.

# Entregables
1. Un único conjunto de datos enriquecido que garantice los mejores resultados cuando entrenemos el algoritmo de clasificación (se espera que realices ingeniería de características).
2. El script de Python utilizado para procesar los datos
3. Algunas consideraciones sobre los datos y el problema, y una breve explicación de tu proceso de pensamiento presentado como una simple Data App creada con nuestro SDK. Ver aquí:

    * [API Shimoku](https://github.com/shimoku-tech/shimoku-api-python)
    * [Documentation](https://docs.shimoku.com/development/getting-started/quickstar)


# Repository structure
The current structure of the repository is essentially the structure recommended by the event organizers with some minor additions:

```
Shimoku_Technical_Test_DS
|   .env
|   .gitignore
|   DS Technical Test Q4-2023.pdf
|   README.md
|   requirements.txt
|
+---data
|       leads.csv
|       offers.csv
|       output_preprocesing.csv
|
+---src
|       dataviz.ipynb
|       dataviz.py
|       Preprocesing.ipynb
|
\---venv
```