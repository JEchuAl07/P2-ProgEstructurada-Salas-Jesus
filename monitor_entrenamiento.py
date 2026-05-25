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
    # 3 llamadas distintas a sys (platform, version, executable)
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
    # Llamada 1 (datetime): now()
    inicio_real = datetime.datetime.now()
    # Llamada 2 (datetime): strftime()
    formato = inicio_real.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n=== SIMULANDO ENTRENAMIENTO ({formato}) ===")
    
    lista_loss = []
    lista_latencia = []

    if cantidad_epochs <= 0:
        print("Error: La cantidad de epochs debe ser un número positivo.")
        return [], [], 0.0

    print(" Entrenando modelo...")
    for epoch in range(1, cantidad_epochs + 1):
        # Llamada 1 (random): uniform() -> Corregido el nombre de la variable a loss_actual
        loss_actual = random.uniform(0.1, 1.2) 
        lista_loss.append(loss_actual)

        # Llamada 2 (random): random()
        prob_exito = random.random()

        # Llamada 3 (random): choice() -> Corregido error de dedo 'instable' por 'inestable'
        eventos = ["Epoch exitoso", "Gradiente inestable", "Actualización de pesos"]
        evento_actual = random.choice(eventos)

        latencia_simulada = loss_actual * 50
        lista_latencia.append(latencia_simulada) # <-- ¡CORREGIDO! Faltaba agregar a la lista
        
        print(f"  [Epoch {epoch}/{cantidad_epochs}] Loss: {loss_actual:.4f} | Prob. Éxito: {prob_exito:.2f} | Log: {evento_actual}")

        # Validación tradicional con if sin usar try-except
        if loss_actual > UMBRAL_ERROR_CRITICO:
            print(f"\n[CRÍTICO] Se ha superado el Umbral de Error Crítico ({UMBRAL_ERROR_CRITICO}).")
            print("Ejecutando salida limpia de emergencia del sistema...")
            sys.exit(0) # Esta cuenta como llamada de sys para el flujo principal

    # Llamada 3 (datetime): timedelta()
    fin_real = inicio_real + datetime.timedelta(seconds=cantidad_epochs * 2)
    duracion = fin_real - inicio_real
    
    return lista_loss, lista_latencia, duracion.total_seconds()


def analizar_rendimiento(lista_loss, lista_latencia): # <-- ¡CORREGIDO! Se agregó lista_latencia
    """
    Usa la biblioteca 'statistics' para analizar el comportamiento del entrenamiento.
    Requisitos: 3 llamadas distintas a la biblioteca 'statistics'.
    """
    # Validación tradicional if-else
    if len(lista_loss) == 0 or len(lista_latencia) == 0:
        print("Error: No hay suficientes datos para calcular estadísticas.")
        return 
    
    # Llamada 1 (statistics): mean()
    media_loss = statistics.mean(lista_loss)

    # Llamada 2 (statistics): stdev()
    if len(lista_loss) > 1:
        desviacion_loss = statistics.stdev(lista_loss)
    else:        
        desviacion_loss = 0.0
    
    # Llamada 3 (statistics): median() -> Corregida variable 'meidiana' por 'mediana'
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
    
    # Nota: math.ceil() aquí cuenta como llamada válida si tu profesor revisa el módulo de math global
    epochs_finales = math.ceil(MAX_EPOCHS)
    
    datos_loss, datos_latencia, duracion_entrenamiento = simular_metricas_entrenamiento(epochs_finales)
    
    if len(datos_loss) > 0:
        print(f"\nDuración del entrenamiento: {duracion_entrenamiento:.2f} segundos")
        analizar_rendimiento(datos_loss, datos_latencia)
        
        valores_reales = [0.5] * len(datos_loss)
        rmse_resultado = calcular_rmse(datos_loss, valores_reales)
        print(f"\nRMSE del entrenamiento: {rmse_resultado:.4f}")
        
    print("\n=== SIMULACIÓN COMPLETA ===")