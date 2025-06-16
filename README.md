# 📊 EDA - ANALISIS EXPLORATORIO DE DATOS
### **Campaña de Marketing Bancario - Portugal**

## 📝 Descripcion del Proyecto 
Este proyecto realiza un analisis exploratorio de datos (EDA) sobre una base de dados de marketing telefónico realizadas por una institución bancaria portuguesa. El objetivo principal es entender el comportamiento de los clientes y los factores que influyen la decision de suscribirse o no a un deposito a plazo fijo. 

## 📁 Dataset
- Archivos usados: bank-additional.csv & customer-details.xlsx
- Filas: 43.000 registros
- Variable: 21 columnas incluyendo características del cliente, del contexto económico y del historial de contacto.

### 📌 Variables claves (dataset)

 1. age: La edad del cliente.
 2. job: La ocupación o profesión del cliente.
 3. marital: El estado civil del cliente.
 4. education: El nivel educativo del cliente.
 5. default: Indica si el cliente tiene algún historial de incumplimiento de pagos (1: Sí, 0: No).
 6. housing: Indica si el cliente tiene un préstamo hipotecario (1: Sí, 0: No).
 7. loan: Indica si el cliente tiene algún otro tipo de préstamo (1: Sí, 0: No).
 8. contact: El método de contacto utilizado para comunicarse con el cliente.
 9. duration: La duración en segundos de la última interacción con el cliente.
 10. campaign: El número de contactos realizados durante esta campaña para este cliente.
 11. pdays: Número de días que han pasado desde la última vez que se contactó con el cliente durante esta campaña.
 12. previous: Número de veces que se ha contactado con el cliente antes de esta campaña.
 13. poutcome: Resultado de la campaña de marketing anterior.
 14. emp.var.rate: La tasa de variación del empleo.
 15. cons.price.idx: El índice de precios al consumidor.
 16. cons.conf.idx: El índice de confianza del consumidor.
 17. euribor3m: La tasa de interés de referencia a tres meses.
 18. nr.employed: El número de empleados.
 19. y: Indica si el cliente ha suscrito un producto o servicio (Sí/No).
 20. date: La fecha en la que se realizó la interacción con el cliente.
 21. latitude: aparentemente un error en el archivo, no corresponde.
 22. longitude: aparentemente un error en el archivo, no corresponde.
 23. id_: Un identificador único para cada registro en el dataset.

 ### 📌 Variables claves (generadas)
 1. education_grouped: agrupacion de la columna 'education' para mantener distinciones relevantes entre niveles bajos, medios y altos de educación.
 2. campaign_capped: limpieza y agrupacion de la columna campaign, eliminacion de ouliers y limitacion a 10 (maximo razonable)
 3. emp_var_context: transformacion de la columna 'emp.var.rate' a una columna categorica y agrupacion de valores para un contexto econmico.
 4. conf_idx_cat: transformacion a categorica de la columna 'cons.conf.idx' y agrupacion en niveles para analizar mejor el indice de confianza del consumidor. 
 5. euribor_cat: transformacion a categorica de la columna 'cons.conf.idx' y agrupacion en niveles para analizar mejor el impacto de la tasa de interes en el consumidor. 
 6. year: segmentacion de la variable año, proveida de la columna date.
 7. y_bin: versión binarizada de la variable objetivo 'y', que originalmente muestra valores de texto (yes & no)

## 📈 Analisis Realizado
- Analisis preliminar
- Limpieza de datos: tratamiento de valores nulos, outliers y codificacion. 
- Analisis univariado: distribucion de variables numericas y categoricas.
- Analisis bivariado: tasa de conversión segun variables claves. 
- Analisis temporal: suscripciones a lo largo del tiempo.
- Segmentaciones: impacto de la economia en el compartamiento del cliente.

## 🧰 Tecnologías usadas
- Python 
- Pandas
- Numpy
- Seaborn
- Matplotlib
- Jypter Notebook

## 📂 Estructura del Proyecto
│
├── DATA/
│    └── RAW
│          └── bank-additional.csv
│          └── customer-details.xlsx
│    └── OUTPUT
│          └── bank-additional_limpio.csv
├── NOTEBOOK/
│    └── 01-analisis_preliminar.ipynb
│    └── 02-limpieza.ipynb
│    └── 03-EDA.ipynb
├── README.md   
├── SRC/
│  └── soporte.py

## ✅ Principales Hallazgos
Los clientes que adquirieron el servicio en su mayoria son de 30 a 38 años, de ocupacion admin y technician, casados y con una educacion superior/tecnica, con una leve recesion en la tasa de variacion de empleo.
Concluimos en que tenemos mayor probabilidad de vender los servicios cuando:
- la tasa de interes es baja
- el contacto con los clientes es de un maximo de 3
- Contrario a lo esperado, vemos que durante periodos de mayor recesión económica —medida por una tasa de variación del empleo más negativa— la tasa de conversión hacia la suscripción es más alta. 
- Si el cliente cuenta con algun tipo de prestamo es menos probable que adquiera el servicio.
- No se visualiza mucha importancia en las variables de cantidad de hijos/adolescentes para adquirir el servicio. Tampoco hay gran difernecia con la variable de 'income' pero podemos mencionar que los clientes con un ingreso entre 85.000 y 124.000 tienen mayores probabilidades de adquirir el servicio.
- Vemos mayor relevancia en la cantidad de años del cliente con la empresa, los clientes nuevos con 0 a 2 ańos de antiguedad tienen mayores probabilidades de adquirir el servicio seguidos de los de 3 a 4 años.

## 📌 Próximos pasos
- Conseguir mayor informacion del performance de campañas pasadas para analizar comportamientos.
- Segmentacion de clientes (clustering)
- Entrenamientos de modelos de clasificacion para predecir mejor la variable "y"