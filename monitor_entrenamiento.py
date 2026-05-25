"""
Nombre del Alumno: Jesús Francisco Salas Palmeros
Matrícula: [Tu Matrícula]
Fecha: 25 de Mayo de 2026
Examen Segundo Parcial - Programación Estructurada
"""
# ==========================================
# 1. IMPORTACIÓN DE BIBLIOTECAS ESTÁNDAR
# ==========================================
import datetime
import math
import random
import statistics
import sys

# ==========================================
# 2. DEFINICIÓN DE CONSTANTES
# ==========================================
MAX_EPOCHS = 10
UMBRAL_ERROR_CRITICO = 0.95

# ==========================================
# 3. FUNCIONES DEFINIDAS POR EL USUARIO
# ==========================================
def obtener_info_sistema():
    """
    Usa la biblioteca 'sys' para validar el entorno de ejecución.
    Requisitos: Realizar 3 llamadas distintas a la biblioteca 'sys'.
    """
    print("\n=== INFORMACIÓN DEL SISTEMA ===")
    plataforma = sys.platform
    version_python = sys.version
    executable = sys.executable
    
    print(f"Plataforma: {plataforma}")
    print(f"Versión de Python: {version_python}")
    print(f"Ejecutable: {executable}")

    if not version_python.startswith("3."):
        print("Error: Este programa requiere Python 3.x.")
        return False
    else:
        print("Entorno de ejecución válido.")
        return True


def simular_metricas_entrenamiento(cantidad_epochs):
    """
    Usa las bibliotecas 'random' y 'datetime' para simular los datos de entrenamiento.
    Requisitos: 3 llamadas a 'random' y 3 llamadas a 'datetime'.
    """
    inicio_real = datetime.datetime.now()
    formato = inicio_real.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n=== SIMULANDO ENTRENAMIENTO ({formato}) ===")
    
    lista_loss = []
    lista_latencia = []

    if cantidad_epochs <= 0:
        print("Error: La cantidad de epochs debe ser un número positivo.")
        return [], [], 0.0

    print(" Entrenando modelo...")
    for epoch in range(1, cantidad_epochs + 1):
        loss_actual = random.uniform(0.1, 1.2) 
        lista_loss.append(loss_actual)

        prob_exito = random.random()

        
        eventos = ["Epoch exitoso", "Gradiente inestable", "Actualización de pesos"]
        evento_actual = random.choice(eventos)

        latencia_simulada = loss_actual * 50
        lista_latencia.append(latencia_simulada) 
        
        print(f"  [Epoch {epoch}/{cantidad_epochs}] Loss: {loss_actual:.4f} | Prob. Éxito: {prob_exito:.2f} | Log: {evento_actual}")

        
        if loss_actual > UMBRAL_ERROR_CRITICO:
            print(f"\n[CRÍTICO] Se ha superado el Umbral de Error Crítico ({UMBRAL_ERROR_CRITICO}).")
            print("Ejecutando salida limpia de emergencia del sistema...")
            sys.exit(0) 

    fin_real = inicio_real + datetime.timedelta(seconds=cantidad_epochs * 2)
    duracion = fin_real - inicio_real
    
    return lista_loss, lista_latencia, duracion.total_seconds()


def analizar_rendimiento(lista_loss, lista_latencia): 
    """
    Usa la biblioteca 'statistics' para analizar el comportamiento del entrenamiento.
    Requisitos: 3 llamadas distintas a la biblioteca 'statistics'.
    """
    # Validación tradicional if-else
    if len(lista_loss) == 0 or len(lista_latencia) == 0:
        print("Error: No hay suficientes datos para calcular estadísticas.")
        return 
    
    media_loss = statistics.mean(lista_loss)

    if len(lista_loss) > 1:
        desviacion_loss = statistics.stdev(lista_loss)
    else:        
        desviacion_loss = 0.0
    
    
    mediana_latencia = statistics.median(lista_latencia)

    print("\n=== REPORTE ESTADÍSTICO ===")
    print(f"Media del Loss: {media_loss:.4f}")
    print(f"Desviación Estándar del Loss: {desviacion_loss:.4f}")
    print(f"Mediana de la Latencia: {mediana_latencia:.2f} ms")


def calcular_rmse(predicciones, reales):
    """
    Usa la biblioteca 'math' para calcular el Root Mean Squared Error (RMSE).
    Requisitos: 3 llamadas distintas a la biblioteca 'math'.
    """
    if len(predicciones) != len(reales):
        print("Error: Las listas de predicciones y reales deben tener la misma longitud.")
        return 0.0

    suma_diferencias = 0.0
    for i in range(len(predicciones)):
        diferencia = predicciones[i] - reales[i]
        # Llamada 1 (math): pow()
        suma_diferencias += math.pow(diferencia, 2)
    
    media_diferencias = suma_diferencias / len(predicciones)

    # Llamada 2 (math): sqrt()
    rmse_final = math.sqrt(media_diferencias)
 
    # Llamada 3 (math): fabs()
    rmse_absoluto = math.fabs(rmse_final)
 
    return rmse_absoluto
    

# ==========================================
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA)
# ==========================================
if __name__ == "__main__":
    print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===")

    obtener_info_sistema()
    
    epochs_finales = math.ceil(MAX_EPOCHS)
    
    datos_loss, datos_latencia, duracion_entrenamiento = simular_metricas_entrenamiento(epochs_finales)
    
    if len(datos_loss) > 0:
        print(f"\nDuración del entrenamiento: {duracion_entrenamiento:.2f} segundos")
        analizar_rendimiento(datos_loss, datos_latencia)
        
        valores_reales = [0.5] * len(datos_loss)
        rmse_resultado = calcular_rmse(datos_loss, valores_reales)
        print(f"\nRMSE del entrenamiento: {rmse_resultado:.4f}")
        
    print("\n=== SIMULACIÓN COMPLETA ===")

"""
==============================================================================
CUESTIONARIO DE ANÁLISIS DE BIBLIOTECAS
==============================================================================

1. Uso de Objetos y Métodos: En tu código, al usar datetime.datetime.now(),
¿cuál es el objeto/clase y cuál es el método que estás llamando? Explica
cómo se relaciona esto con el concepto de biblioteca externa.

El primer "datetime" hace referencia al módulo o biblioteca que hemos importado,
mientras que el segundo "datetime" se refiere a la clase dentro de esa biblioteca. 
El método "now()" es una función de clase que devuelve la fecha y hora actuales. 
Esto demuestra cómo las bibliotecas externas proporcionan objetos y métodos 
predefinidos que podemos utilizar para realizar tareas específicas sin tener que 
programar todo desde cero.

2. Diferenciación Técnica: ¿Qué diferencia existe en la sintaxis de tu código
al importar un módulo completo (ej: import math) versus importar un método
específico (ej: from math import sqrt) al momento de invocar sus funciones?

Cuando usamos "import math", se carga el módulo completo por lo que estamos obligados a usar
el prefijo del módulo en cada invocación. En cambio, con "from math import sqrt", 
solo importamos la función específica y podemos usarla directamente sin el prefijo del módulo.

3. Flujo y Lógica: Describe brevemente la secuencia lógica de pasos que
implementaste para conectar los datos generados por tu función de
simulación con la función que calcula el error (RMSE).

La funcio "simular_metricas_entrenamiento" genera listas de datos de loss y latencia, que luego son
pasados a la función "analizar_rendimiento" para obtener estadísticas. Finalmente, los datos de loss 
se comparan con valores reales en la función "calcular_rmse" para obtener el error del modelo.

4. Mapeo de Tipos de Datos: Identifica al menos dos tipos de datos
complejos (colecciones) que utilizaste para organizar los resultados de tus
análisis y justifica por qué elegiste esa estructura en lugar de variables
simples.

Se implementaron listas para almacenar "lista_loss" y "lista_latencia" de cada epoch.
Se eligieron listas porque permiten almacenar múltiples valores de manera ordenada y 
son fáciles de iterar para cálculos estadísticos posteriores, a diferencia de 
variables simples que solo podrían almacenar un valor a la vez.

5. Autoevaluación de Abstracción: Al utilizar las funciones de la biblioteca
statistics, ¿tuviste que programar la fórmula matemática matemática de la
desviación estándar? Relaciona esto con el concepto de Abstracción visto
en clase.

No, no tuve que programar la fórmula matemática de la desviación estándar, ya que la función 
"statistics.stdev()" se encarga de realizar ese cálculo internamente. 
Esto es un ejemplo claro de abstracción, donde el usuario puede utilizar 
una función sin necesidad de entender o implementar detalles matemáticos, lo que simplifica 
el proceso y permite enfocarse en el análisis de los resultados en lugar de en la 
implementación de fórmulas complejas.
"""